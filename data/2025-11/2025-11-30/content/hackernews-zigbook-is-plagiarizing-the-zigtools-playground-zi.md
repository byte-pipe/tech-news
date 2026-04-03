---
title: Zigbook is Plagiarizing the Zigtools Playground - zigtools
url: https://zigtools.org/blog/zigbook-plagiarizing-playground/
site_name: hackernews
fetched_at: '2025-11-30T19:07:00.861001'
original_url: https://zigtools.org/blog/zigbook-plagiarizing-playground/
author: todsacerdoti
date: '2025-11-30'
description: 'zigtools: We make free and open-source tools for the @ziglang community.'
---

# Zigbook is Plagiarizing the Zigtools Playground

Auguste Rame,Techatrix— 30 November 2025

## Introduction

For those unfamiliar, Zigtools was founded to support theZigcommunity, especially newcomers, by creating editor tooling such asZLS, providing building blocks for language servers written in Zig withlsp-kit, working on tools like theZigtools Playground, and contributing to Zig editor extensions likevscode-zig.

## The Plagiarism

A couple weeks ago, a Zig resource called Zigbook was released with a bold claim of “zero AI” and an original “project-based” structure.

Unfortunately, even a cursory look at the nonsense chapter structure, book content, examples, generic website, or post-backlash issue-disabled repo reveals that the book is wholly LLM slop and the project itself is structured like some sort of sycophantic psy-op, with botted accounts and fake reactions.

We’re leaving out all direct links to Zigbook to not give them any more SEO traction.

We thought that thebroad community backlashwould be the end of the project, but Zigbook persevered, releasing just last week a brand new feature, a “high-voltage beta” Zig playground.

As we at Zigtools have our own Zig playground (repo,website), our interest was immediately piqued. The form and functionality looked pretty similar and Zigbook even integrated (in a non-functional manner) ZLS into their playground to provide all the fancy editor bells-and-whistles, like code completions and goto definition.

Knowing Zigbook’s history of deception, we immediately investigated the WASM blobs. Unfortunately, the WASM blobs are byte-for-byte identical to ours. This cannot be a coincidence given the two blobs (zig.wasm, a lightly modified version of the Zig compiler, andzls.wasm, ZLS with a modified entry point for WASI) are entirely custom-made for the Zigtools Playground.

We archived the WASM files for your convenience, courtesy of the great Internet Archive:

* zls.wasm(sha256sum:3a63e5092e8f90172716977af5c88b4f49e546f730f25e9bafb47f4ac9a2ee1d)OriginalPlagiarized
* Original
* Plagiarized
* zig.wasm(sha256sum:d3fe6b8a6b1db84a914eaa1f4a80ca5dcfd3b0948a35f2b1e78432a392eace96)OriginalPlagiarized
* Original
* Plagiarized

We proceeded to look at the JavaScript code, which we quickly determined was similarly copied, but with LLM distortions, likely to prevent the code from being completely identical. Still, certain sections were copied one-to-one, like the JavaScript worker data-passing structure and logging (original ZLS playground code,plagiarized Zigbook code).

The following code from both files is identical:


try

{


// @ts-ignore


const

exitCode

=

wasi
.
start
(
instance
)
;


postMessage
(
{


stderr
:
`\n\n---\nexit with exit code
${
exitCode
}
\n---\n`
,


}
)
;


}

catch

(
err
)

{


postMessage
(
{

stderr
:
`
${
err
}
`

}
)
;


}


postMessage
(
{


done
:
true
,


}
)
;


// ...


onmessage

=

(
event
)

=>

{


if

(
event
.
data
.
run
)

{


run
(
event
.
data
.
run
)
;


}


}
;

The\n\n---\nexit with exit code ${exitCode}\n---\nis perhaps the most obviously copied string.

Funnily enough, despite copying many parts of our code, Zigbook didn’t copy the most important part of the ZLS integration code, the JavaScript ZLS API designed to work with theZLS WASM binary’s API. That JavaScript code is absolutely required to interact with the ZLS binary which theydidplagiarize. Zigbook either avoided copying that JavaScript code because they knew it would be too glaringly obvious, because they fundamentally do not understand how the Zigtools Playground works, or because they plan to copy more of our code.

To be clear, copying our code and WASM blobs is entirely permissible given that the playground and Zig are MIT licensed. Unfortunately, Zigbook has not complied with the terms of the MIT license at all, and seemingly claims the code and blobs as their own without correctly reproducing the license.

We sent Zigbook a neutralPR correcting the license violations, but they quickly closed it and deleted the description, seemingly to hide their misdeeds.

The original description (also available in the “edits” dropdown of the original PR comment) is reproduced below:

We (@zigtools) noticed you were using code from the Zigtools Playground, including byte-by-byte copies of our WASM blobs and excerpts of our JavaScript source code.

This is a violation of the MIT license that the Zigtools Playground is licensed under alongside a violation of the Zig MIT license (for the zig.wasm blob).

As the MIT license states:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

We’ve fixed this by adding the licenses in question to your repository. As your repository does not include a direct link to the *.wasm dependencies, we’ve added a license disclaimer on the playground page as well that mentions the licenses.

Zigbook’s aforementioned bad behavior and their continued violation of our license and unwillingness to fix the violation motivated us to write this blog post.

## Our Vision for the Zigtools Playground

It’s sad that our first blog post is about the plagiarism of our coolest subproject. We challenged ourselves by creating a WASM-based client-side playground to enable offline usage, code privacy, and no server costs.

This incident has motivated us to invest more time into our playground and has generated a couple of ideas:

* We’d like to enable multifile support to allow more complex Zig projects to be run in the browser
* We’d like to collaborate with fellow Ziguanas to integrate the playground into their excellent Zig tutorials, books, and blogpostsA perfect example usecase would be enabling folks to hop intoZiglingsonline with the playgroundThe Zig website itself would be a great target as well!
* A perfect example usecase would be enabling folks to hop intoZiglingsonline with the playground
* The Zig website itself would be a great target as well!
* We’d like to support stack traces using DWARF debug info which is not yet emitted by the self-hosted Zig compiler

## Conclusion

As Zig community members,we advise all other members of the Zig community to steer clear of Zigbook.

If you’re looking to learn Zig, we strongly recommend looking at the excellent officialZig learn pagewhich contains excellent resources from the previously mentionedZiglingstoKarl Seguin’s Learning Zig.

We’re also using this opportunity to mention that we’re fundraising to keep ZLS sustainable for our only full-time maintainer, Techatrix. We’d be thrilled if you’d be willing to give just $5 a month. You can check out ourOpenCollectiveorGitHub Sponsors.

Thanks for reading! \(^-^)/

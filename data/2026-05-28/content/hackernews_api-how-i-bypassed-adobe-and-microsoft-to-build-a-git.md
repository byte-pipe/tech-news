---
title: How I Bypassed Adobe and Microsoft to Build a Git-Tracked Book Production Pipeline | D. J. Speckhals
url: https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/
site_name: hackernews_api
content_file: hackernews_api-how-i-bypassed-adobe-and-microsoft-to-build-a-git
fetched_at: '2026-05-28T06:03:22.149455'
original_url: https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/
author: dustin1114
date: '2026-05-23'
published_date: '2026-05-22T10:05:54-04:00'
description: How a software developer bypassed proprietary publishing silos using LibreOffice, Standard Ebooks, and LaTeX to build a sustainable, Git-tracked book production pipeline.
tags:
- hackernews
- trending
---

The most important piece of fiction writing is the story. Are the characters compelling? Is the plot exciting and coherent? Is the story believable? Paired with that is writing quality, which includes grammar, syntax, spelling, and punctuation. Without an immense amount of work on these points, authors lack a book worth publishing.

Formatting and typesetting a novel can become an afterthought. It’s probably the most technology-driven part of the self-publishing process, which can be scary to authors who just want to get a polished book into readers’ hands. I don’t mean to imply my formatting process is the best or the easiest. It works for me and satisfies my inclinations as both an independent novelist and software developer.

## Word + InDesign + Calibre + Kindle Create

I started safe. All three of my Christian historical novels—Heretics of Piedmont,The Lord of Luserna, andPrince of Savoy, plus my novellaThe Outcast of Chivasso—started as Microsoft Word files (DOCX). The vast majority of editors and proofreaders rely on Word for tracked changes, and practically every final formatting program (Adobe InDesign, Kindle Create, Calibre, Atticus, etc.) can import DOCX files. Like a good boy, I used paragraph styles rather than manual formatting. My Word document—named something like “Heretics-of-Piedmont_revised-final-3.docx”—became my source of truth, the common ancestor for all final formats.

I didn’t want to format my book for print in Word, though. Can it be done? Yes. Does it meet the quality standards of professionals? That’s debatable. Its hyphenation and justification leave a lot to be desired, among other weaknesses. The last time I checked (early 2026), Word doesn’t includemicrotypographyfeatures like desktop publishing software does.

Other options exist, but Adobe InDesign is the industry standard. Professionals use its battle-tested feature set to produce what truly can be art. I wanted that level of quality in my own books. So I held my nose and plunged into the world of Adobe Creative Cloud. I didn’t know how to use InDesign at first, but I read a lot and watched plenty of YouTube videos on the craft. I learned about DOCX style mapping, preventing em-dash breaks, crisp margins, page balancing, attractive drop-caps, tracking, optical margins, baseline grids, and other minutia. Plenty of jargon there, but the work is quite satisfying, especially when you notice the details in the end product. (Side note: when I browse bookstores, I always investigate how big publishing houses do it.) When I got to the sequels, I again chose InDesign.

Ebooks are an entirely different matter. There are many decent options to produce an EPUB, but none seem to dominate ebook publishing like InDesign does for print.Kovid Goyalis a familiar name in the software world; he’s one of those talented developers who make working with computers better for the rest of us. Perhaps his most well-known contribution isCalibre, a powerful ebook manager. Not only can you read nearly any ebook with it, but it also includes an amazing ebook authoring toolset. Importing from a Microsoft Word document is a breeze, and with a little HTML and CSS knowledge, you can create a very compatible EPUB.

Kindle is a different story. Youcanupload EPUBs to Kindle Direct Publishing (KDP), where they will convert it into their proprietary KFX file. I never had success uploading the EPUBs I had created with Calibre, however. Amazon’s suggested solution is theirKindle Createprogram, which worked okay, but that was yet another format to maintain. The software developer in me was screaming for a better solution.

## Opportunities

Making the slightest change became a chore.

* Update the “master” DOCX
* Update InDesign file, export PDF, upload to distributors
* Update EPUB in Calibre, export EPUB, upload to distributors
* Update in Kindle Create, export KPF, upload to KDP

A Linux laptop is my daily driver, but neither Kindle Create nor InDesign run on it (even with Wine), so I had to switch to my family Macbook—first-world problems, but I like what I’m used to.

A few years ago onHacker News, I discoveredStandard Ebooks. I read the project’s goals and skimmed a few of their published works. To say I was impressed is an understatement. Their books were miles ahead of any free ebook. I noted the project and have since read at least a dozen books from their growing library of public domain works (by the way, they’re a worthy cause tosupport). If only my own ebooks could match their quality.

## Pivoting

I finishedPrince of Savoy, Book 3 of my trilogy, in 2025 and was ready to format it. As I had done numerous times, I imported the Word document into InDesign and formatted the print version. But then I had an idea—what if I followed Standard Ebooks’ (SE) process instead? For a few reasons, I used Calibre to convert the DOCX to a clean EPUB, to which I would later applySE’s Manual of Stylevia theirdetailed guide to producing an ebook.

I quickly discovered how strict, how pedantic, and how utterly opinionated SE is. Their style guide leaves little room for interpretation or ambiguity, which, if followed properly, results in a pristine EPUB that’s compatible on practically all devices. The process was a chore, especially the first time I worked through it. I told myself, “Trust the process; it’ll be worth it,” because it often felt more like a chore. Looking back, I feel like SE’s tools (all funnelled through the powerfulstandardebookscommand line program) are like having a copyeditor for ebook formatting or a linter for code. Here are some examples from SE’s linter:

* Illegal unit used to setfont-size. Hint: Useemunits.
* Word count in metadata doesn’t match actual word count.
* Header element with incompatible semantics. Hint: Headers should be eithertitleorordinal, not both.
* Possessive’swithin name italics. Hint: If the name in italics is doing the possessing,’sgoes outside italics.

…among hundreds of other checks. The strictness appeals to me as a software developer. Getting all lint rules to pass took some time, but it was satisfying to end up with a clean directory of XHTML source files, version controlled in Git, easily built as an EPUB with these buildcommand. I had scratched Kindle Create from my workflow, because Standard Ebooks EPUBs converts well for Kindles.Prince of Savoywas ready to distribute, and I was thoroughly satisfied with its electronic format.

## Open Source Tooling

With the trilogy complete, I wanted to go back and revise the first installment,Heretics of Piedmont. I spent 3 weeks of free time improving minor details (eliminating a few anachronisms, slimming prose, adding three hand-drawn maps), with the goal of fully matching the style of Books 2 and 3. But I was tired of editing the document on a Windows computer—or worse, Office 365 Online. Pedantically, I performed the conversion from DOCX to ODT (Open Document Text, the native format for LibreOffice Writer).

Does LibreOffice have its shortcomings? Certainly. But from my experience, it does its job: I can type, check spelling and grammar, and perhaps most importantly, apply styles. As I revised, I added semantic paragraph styles for songs, letters, poems, epigraphs, glossary entries, etc.; character styles are a less used feature of word processors, but they can act as semantics that go beyond basic formatting. I created styles for each foreign language (seven of them inHeretics of Piedmont) and applied them to the approximately one hundred non-English phrases in the text. There are also character styles for direct thoughts, creative work titles, prayers, and emphasis; though all of these translate toitalicswhen reading in print and electronically, having these semantics is a key in producing a Standard Ebooks-compliant EPUB. Not only do the semantic attributes make the book more accessible for those who use screen-readers, but they also enable more control that surpasses simple italics formatting.

Now I had a clean, semantically rich ODT file: open source, easy to edit, and as I would soon discover, simple to parse. I chose this file as my “source of truth.” “Why didn’t you just author it in LaTeX? Or Markdown? Or RST?” you might ask. I considered each of those, but I prefer writing novels in a word processor, not a text editor.

Now I needed to create a PDF and an EPUB. Though I had never parsed an ODT file, a little Python, lxml, and Claude Code helped me quickly draft the conversion script. The script maps the XML nodes of the ODT file to an intermediary structure, which then allows for easily output to XHTML (and eventually LaTeX; I’ll get to that later). I ran the conversion script with a TOML config file (which maps ODT styles to XHTML elements and attributes), and I had everything I needed for the SE EPUB—and only a couple lint errors to fix. Ebook goal accomplished!

The more difficult path was the print PDF. I desperately wanted LibreOffice Writer to have the features I needed. Coincidentally, several microtypography features landed in 2025 that sounded much like Adobe InDesign’s capabilities. Would it be that simple?

Unfortunately, no. Though I read through changelogs and saw the care volunteer developers took in bringing microtypography to Writer, it wasn’t up to the task yet. The end edge of the page was ragged, the bottom edge was unbalanced, and drop caps appeared odd. I tried Scribus too, but 200+ page books bring the program to a crawl. And the results were worse than Writer. I’d have to settle for InDesign, I figured.

Then I thought ofLaTeX. I had heard of it since I started programming but was never fully exposed to it. In college (non-STEM), I submitted papers as Word documents or PDFs. LaTeX seemed daunting, but it had the features I desperately wanted: advanced typography, ability to automate, and version control. I tested a chapter from my book as LaTeX and compared the output with Adobe InDesign’s. It was nearly indistinguishable.

Now the hard part: How do I convert an ODT file to TeX?Pandoccan, but custom Writer styles aren’t carried over. So I repurposed the same conversion script I used for ODT→XHTML and generalized it to support ODT→TeX. Perhaps some day I’ll open source that code, but it’s currently tailored for my own unique use cases, and I’m not sure it will help others yet.

## Retrofitting

At last I had a sustainable, automated, version-controlled path for producing print and electronic versions of my books—without proprietary software like Word and InDesign. There’s still the downside of having to edit the “master” ODT file, then regenerating the PDF and EPUB, but it’s a trivial process I can perform on any computer. I had transitioned from opaque binary(ish).docxand.inddfiles to plain-text.xhtmland.tex. Seeing exactly what changed in a proofreading pass viagit diffwas a massive quality-of-life win.

Even though I had revised and “retooled”Heretics of Piedmont, I still had two other novels and a novella that used the old tools. I also converted those Word documents to semantic Writer documents, then my conversion script handles the rest.

Is there room for improvement? For sure. I would love if the XHTML and TeX were artifacts rather than code. I currently have separate Git repositories for the XHTML and TeX for each book, mainly because I want the ODT file to remain the source of truth. It’s easier for me to write in, and professional copyeditors and proofreaders want word processor documents for their work.

My process certainly isn’t for everyone. Most independent authors would be fine with either hiring a professional formatter or settling with something similar to my earlier process. In the end, readers don’t care about the formatting process. They want to read a good story. I want to provide that first, but if I can also enjoy the formatting, I’ll count that as a win for my readers too.

## Appendix: The LaTeX Preamble

For anyone interested in the underlying mechanics, you canview the full LaTeX preamble here.

These are the key packages I used:

* memoir: “batteries included” class for document creation
* fontspec: allows rendering of OpenType fonts (like my favorite body text,Adobe Garamond)
* polyglossia: provides hyphenation patterns per language; I occasionally use non-English languages like Old Occitan and Latin for reader immersion
* graphicx: allows advanced embedding and adjustment of images like maps and my author portrait
* microtype: provides the previously-mentioned features that enhance the appearance and readability of every page—one of the main reasons I chose LaTeX

* LaTeX
* TeX
* EPUB
* Standard Ebooks
* Novel Formatting
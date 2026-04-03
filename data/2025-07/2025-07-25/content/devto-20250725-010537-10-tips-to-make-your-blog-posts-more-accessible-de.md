---
title: 10 Tips to Make Your Blog Posts More Accessible - DEV Community
url: https://dev.to/eevajonnapanula/10-tips-to-make-your-blog-posts-more-accessible-1o7m
site_name: devto
fetched_at: '2025-07-25T01:05:37.281823'
original_url: https://dev.to/eevajonnapanula/10-tips-to-make-your-blog-posts-more-accessible-1o7m
author: Eevis
date: '2025-07-18'
description: Sometimes I encounter this weird idea that developers don't need accessibility at all. Some people... Tagged with writing, a11y, html, inclusion.
tags: '#writing, #a11y, #html, #inclusion'
---

Sometimes I encounter this weird idea that developers don't need accessibility at all. Some people seem to believe that our development tools and resources don't need to be accessible, because accessibility is just something to do with the end users of our services.

If you're one of those people, you know, disabled software developers exist. You're reading text from one right now, and I know many developers with disabilities. Yes, even blind developers.

I've been writing a blog since 2019, and as an accessibility specialist, I've tried to make my blog posts as accessible as possible. In this blog post, I decided to share some of the things I've learned over the years. So, without further ado, let's get started.

## Share Code as Text, not as Images

If you're writing a technical blog post and sharing some code, always write it as text, never share it as an image. Why? There are multiple reasons.

First of all, it's super annoying to copy the code from a blog post if it's an image. The reader would need to type it out, instead of just copying and pasting. At least for me, when I'm sharing code in a blog post, it's meant to be used, and the fastest way is to use copy and paste.

Images of code are also an accessibility problem. With an image, there is no way to make the text bigger, change colors for better contrast, or modify the text row length. All of these are things people might need to make the web content more accessible for them.

And then there's the text alternative part - if you're sharing an image of text, you should always include the text as text alternative (alt text) for the image. However, even if you include code, the way screen readers interact with alt texts makes it more challenging to use. E.g., navigating within the code is harder because screen readers read the text from the beginning, and it's not really possible to jump from one row to another.

So, always put code into a code block as text. Most blogging platforms allow this, and if you have your own website, semantic HTML also has these tags (hint:<code>) for including code without running it.

I mentioned alt text or text alternatives - if you're unfamiliar with the concept, I'll explain it in the next section.

## Write Text Alternatives for Graphics

The next tip I'm going to give is to write text alternatives for images. Usually, blogging platforms allow this, and if you're using markdown, you can write it in the first brackets of the image. So,

![Alt text goes here](image url)

And if you're writing in pure HTML, the<img>element has thealtproperty:

<img src="..." alt="Text alternative goes here" />

Enter fullscreen mode

Exit fullscreen mode

Why? Text alternatives are there for people who can't see the picture. And that might include you, even if you're a sighted person. Most importantly, it's for assistive technology, such as screen readers, users. They need the same content as a sighted person can see as text.

It's also useful in cases where the image doesn't load. Slow internet? Yup, been there. If the image has a text alternative, I can still read the article. And all those crawlers that crawl websites can use everything that's in text format, so it's good for SEO and AI search.

And what should you write as the text alternative?WebAIM's Alt text pagehas excellent resources, explaining how, e.g., context affects the decision, and what decorative images are.

## Use Readability Score to Guide Your Writing

When you're writing a blog post, I wholeheartedly recommend using tools likeHemingwayorGrammarlyfor grammar. Additionally, they're great for getting a readability score for your text. I'll share about it in a bit.

I'm not a native English speaker, and I've relied on Grammarly for writing and checking my grammar for the whole time I've been writing blog posts. Nowadays, it complains less (I guess I've learned something, yay!), and it's been extremely helpful in producing better text. And no, I'm not using the generative AI features. I want to write my own text.

The readability score is a fantastic feature. It gives a score on how easy the text is to read, which helps to tailor the content for better, you guessed it, readability.

There are different scoring methods. The idea for all of them is to give a score indicating the education level the reader should have to understand the text easily. If you want to know more about the different methods, Flesch-Kincaid Grade Level and Flesch Reading Ease score are good search terms to start your explorations.

And okay, now you might think that for technical content, the education level should be university-level, as everyone in this field has at least a bachelor's degree. Okay, I really do hope you don't think that, because not everyone does.

We're reading texts in different situations. If the text is written in a way that it's readable for an eighth-grader, it also helps anyone who's, e.g., under stress to understand the text better. And I don't know about any of you, but for me, being stressed has been a large part of being a software developer.

Oh, and if you're wondering, the readability score of this text is 69 on Grammarly. It translates roughly to 8th grade, as Grammarly uses Flesch reading ease scoring.

## List Links at The End

My next tip is to list all the links included within the text at the end of either a section or the blog post. For some people, it might be hard to see links inside a paragraph. This is especially true if the link styles don't differ that much from the text styles, e.g. the link is annotated only with a (slight) color change and lacks underlining.

And when you do list the links, use the same link text as in the original link (so, inside the text). Links leading to the same destination should always have the same text.

As an example, you can find links in this blog post in theLinks in the Blog Postsection.

## Add Table of Contents

Adding a table of contents at the beginning of a blog post is also a way to make the post more accessible. This way, the reader can get a better picture of what the blog post contains. If the table of contents also includes links to each section, they can also navigate to relevant sections more easily.

I have a table of contents in each blog post in the original post that I publish on my website. It's automatically generated from the top-level headings. I've been thinking about copying it to the articles I'm cross-posting, but haven't done so yet.

## Write Clearly and Simply

Writing clearly makes the blog post's content more understandable. It's also connected to the readability score, but it's more than just the length of the sentences and the words used - the factors used in the reading algorithms.

WebAIM provides a good resource on the topic, and I used the title of the page as the title of this section. The resource is available inWebAIM: Writing Clearly and Simply. I'll list the points from WebAIM below; you can read more about each step from the link to WebAIM's page:

1. Organize your ideas into a logical outline—before and during the writing process.
2. Introduce, explain, summarize.
3. Stay on point.
4. Make it interesting.
5. Write for your audience.
6. Assume that your readers are intelligent, but do not assume that they know the subject matter as well as you.
7. Write cohesive paragraphs constructed around a single major idea.
8. Avoid slang and jargon.
9. Use familiar words and combinations of words.
10. Use active voice…
10a. …but not necessarily always.
11. Use forceful verbs.
12. Use parallel sentence construction.
13. Use positive terms.
14. Give direct instructions.
15. Use positive or single-negative phrasing.
16. Explain acronyms and abbreviations; avoid them if possible.
17. Check spelling.
18. Write short sentences.
19. Ensure that every word and paragraph is necessary.
20. When you're finished, stop.

I have to admit that this is something I'm still learning myself. Using tools like Grammarly or Hemingway for writing helps, as they have checks for many of these points. However, I still struggle with some of them regularly. If you feel overwhelmed by the number of things to consider, I recommend using one of the writing tools mentioned and learning one thing at a time.

## Explain Code Examples

If you share examples of code, in addition to giving them in text format, explain them as well. Even if you know what the code does just by looking at it, not everyone knows. Unless you know every single reader of your post and can be sure that they're never, for example, stressed or tired, explaining the code improves cognitive accessibility for readers.

## Use Semantic HTML

This tip is relevant if you have access to the source code, such as when publishing articles on your website.

First of all, use semantic HTML on your website. Seriously, usingdivs for everything is not accessible. Semantic elements provide a lot of functionality and information for accessibility services and different navigation APIs by default, so you don't need to add that information or functionality yourself.

If you want to learn more about semantic HTML, I've written a blog post waaaay back:Ode to Semantic HTML. MDN's Curriculum has alsoa section about Semantic HTML.

## Display Estimated Reading Time

Another tip for sites where you can customise the presentation of the article beyond just the text is to consider adding estimated reading time for the article. Having it at the beginning of the article can help users decide if now is the time to read the article, or if they should return to it later. It also helps to manage expectations - roughly, how long should I expect to spend reading it?

Depending on the technology you're using for building the site, there are tools or plugins for that. For example, my site is built with Eleventy, and I useeleventy-plugin-time-to-readfor calculating the time to read. It's not perfect, but it gives a good enough number for the purposes.

## Consider Adding a Summary

The last tip I'm going to share is to consider adding a short "Too Long, Didn't Read" (TL;DR) type of summary at the beginning of the blog post. This summary provides the reader with an idea of what's in the blog post, whether it's relevant for them, and helps to understand the content better.

I have been planning to add this for a long time, but haven't gotten to it yet, as it has felt hard to summarize the essential points. Like, what's the most important thing in the post? But I intend to explore how well different AI tools would do this, meaning I'll just need to find the right prompt and then check the result to see if it's correct.

## Wrapping Up

In this blog post, I've shared some advice on how to make blog posts more accessible for all. The tips have ranged from the text and content itself to modifying the site itself to make it accessible, if you have access to the website's source code.

Do you have any additional advice? Did you learn something new?

## Links in the Blog Post

* WebAIM's Alt text page
* Hemingway
* Grammarly
* Ode to Semantic HTML
* WebAIM: Writing Clearly and Simply
* a section about Semantic HTML
* eleventy-plugin-time-to-read

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

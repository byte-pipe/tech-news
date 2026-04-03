---
title: Interview with Øyvind Kolås, GIMP developer - GIMP
url: https://www.gimp.org/news/2026/02/22/%C3%B8yvind-kol%C3%A5s-interview-ww2017/
site_name: hnrss
content_file: hnrss-interview-with-øyvind-kolås-gimp-developer-gimp
fetched_at: '2026-03-02T08:25:34.286994'
original_url: https://www.gimp.org/news/2026/02/22/%C3%B8yvind-kol%C3%A5s-interview-ww2017/
date: '2026-02-26'
published_date: '2026-02-22T00:00:00+01:00'
description: Interview with Øyvind Kolås, GIMP developer
tags:
- hackernews
- hnrss
---

## Interview with Øyvind Kolås,GIMPdeveloper

 2026-02-22
 

 by 
GIMP Team
 

GIMPisFree and Libre Open Source Software, but none of it is possible without
the people who create with and contribute to it. Our project maintainerJehanwanted to interview the volunteers
who makeGIMPwhat it is, and share their stories so you can learn more about the awesome people behindGIMP!

Early interviews with co-maintainerMichael NattererandMichael Schumacherwere 
published shortly after the firstWilber Week. Unfortunately, 
the rest of the interviews from that event have never seen the light of day - until now!

Our previously resurfaced interview was withSimon Budig.
The interview in this article is aboutØyvind Kolås. He is the maintainer ofGEGLandbabl, the color engines ofGIMP. His work was instrumental in (amongmanyother things) the 
long-waitednon-destructive filtersimplemented inGIMP3.0!

This interview took place on February 4th, 2017. In addition toJehanandØyvind,Michael Schumacher,Simon Budig, andDebarshi Raywere also involved and asked questions.

Øyvind Kolås, by Michael Schumacher, 
CC
-
BY
-
SA
 - 2019

Jehan: Okay, hello Pippin! So, first off, how should we call you, Pippin or Øyvind?

Øyvind: If people know how to pronounce ‘Øyvind’, that is perhaps easiest. In some contexts it is a difficult name to pronounce and I have to go by my nickname Pippin.

Jehan: Ah, and where does it come from?

Øyvind: The nickname Pippin originates from Lord of the Rings. The first time I went onIRC, must have been ‘95 or ‘96, I had to come up with a nickname for myself, and I chose the nickname of a hobbit. I used the nickname “Sméagol”.

Jehan: But you’re not very small.

Øyvind: No, but Sméagol is the hobbit in terms of Gollum, and I kind of decided that I didn’t want to have the association that came along withthathobbit. So after just one day of using that nickname I skimmed a little bit through the history of the Lord of the Rings again, and noticed that the “Pippin” hobbit might be more appropriate. He’s a hobbit that’s a little bit too curious – he throws stones in Morannon and stares into Saruman’s palantír and wonders how things work.

Jehan: So, how many times have you read Lord of the Rings?

Øyvind: Two or three times? I’ve seen the movies more than once.

Jehan: How are the movies?

Øyvind: They’re okay. They’re long!

Jehan: So, you’re theGEGLmaintainer.Maybe first, let’s explain whatGEGLis. For people who read the website, they may knowGIMP, maybe not necessarilyGEGL.

Øyvind:GEGLis a library or system where you can plug components together. You can createchains of image manipulation filters or operations. So you can first adjust the colors of an image, and then apply some sharpening to it. So you can construct those as a flow chart or similar – “First do this then do that, then do that” – so programmers can create data structures representing such chains or flows of image data, and developers can use such components to use in the chain.

Jehan: And so how did you come into this project?

Øyvind: I had been usingGIMPfor quite a while, and then at some point I was experimenting with writing my own video editor. And I started implementing various transform tools and operations – I implemented perspective rotation tools and similar. And while I was doing that, I was also taking a look at howGIMPwas doing some such transformation tools and operations. And I realized that the perspective transform inGIMPproduced not quite the results that I would like it to produce.

It had big problems with moire and aliasing when you did severe perspective transforms, for instance. So with my newly gained knowledge of making something similar myself, I sat down and tried to figure out how to improve whatGIMPwas doing. So I made a patch fix to add adaptive subdivision super-sampling to the transform tools.

Jehan: So it was notGEGL?

Øyvind: It was forGIMP. That’s how I got involved in theGIMPproject, it was my first patch that I did there. But even that was after I had ran into many of the people from theGIMPproject at aGNOMEconference in Copenhagen in, I believe, 2001.

Jehan: Okay. So, how doesGEGLchangeGIMP? What isGEGLforGIMP?

Øyvind: Well, I’m the wrong person to ask that question. I know howGEGLworks. I know many of the needs ofGIMP. But the person who has the greatest knowledge and detail of howGEGLmakes that work and happen forGIMPisMitch.

Jehan: We should have asked him yesterday then!Thank you. So, maybe you can still explain some of the cool features inGIMP. Like what everyone has been talking about, such as non-destructive editing, which is enabled byGEGL?

Øyvind: So this graph-based data-flow chains of operations that you can do withGEGL– most parts ofGIMPhave been transformed to make use of that. The core thing that is currently non-destructive editing inGIMPis the layers dialog. Other software has more capabilities there, but it’s not easy for us to know what interface to provide and present to the user to add such capabilities as drop shadows, or blurs, or color adjustments.

Jehan: It’s easy or not easy?

Øyvind: It’s easy to do it as a hack or as a proof of concept, but it’s more difficult to figure out how to do it in a way we can guarantee will be stable for many years into the future. So where we are currently, as we are close to being able to releaseGIMP2.10 is that we’re doing all the layer processing thatGIMP2.8 use to do, but there’s no hacks – we’re usingGEGLas the engine instead.

Jehan: So, do you useGIMPa lot?

Øyvind: SometimesGIMPis the appropriate tool, and sometimes there’s other existing software that I use as a tool. And sometimes the tools I want or need don’t exist, and then I try to make those tools.

Jehan: You also have a background as an artist. Could you maybe speak on this?

Øyvind: From when I was a teenager, I’ve been doing both visual arts such as painting and drawing, and being interested in creating media in various forms such as videos. The only form of creative expression that I haven’t much played with is music. My original education and training was in fine arts. Only after having done that for a few years did I go back to computers and digital media, and go more the academic route in computer science.

Jehan: So you studied computer science before, then you went to art?

Øyvind: No, but I’ve been doing computer graphics since I was 14 or 15 years old. I was inspired by the demoscene community and having access to dial-up bulletin boards systems with people discussing programming techniques and languages. They contained tutorials in C and Pascal and Assembly and also involving Turbo Pascal. Demoscene-style graphics are things I’ve done since before University level age, along with experimenting with painting and traditional physical drawing media.

The illusion in this image came as a result of pippin’s
curiosity about images and perception,
and since it went viral on social media, it has been used in new
papers online and in print, books and tv-shows.

Jehan: So how do you see the future ofGEGLand free software graphics in general? How do you seeGEGLin 20 years?

Øyvind: IfGIMPstill exists in 20 years in some form ofUI, then most probablyGEGLis part of that story as well. I hope that some of the existing core processing code actually doesn’t survive! But the idea of the graph and maybe some of the operations that are hooked up to each other, I hope that continues to exist. Just like how other applications that useGEGLlike video editing software,GIMP,GNOMEPhotos – theAPIand how they do that, I hope are very similar. But maybe both theCPUbased processing code and the OpenCL one, will have been replaced.

Jehan: There’s something I’ve never really completely understood. If you look at the GitLab ofGIMPandGEGL, they started around the same time. So why are they getting merged only recently?

Øyvind: I only know stories of this – I haven’t been around in the project since in the beginning.

Michael Schumacher: You said you’re not the best person to ask howGIMPis usingGEGL. So can you tell us how you wish it was being used, or how you think it could be used more? Because I recall you making comments onIRCin that regard.

Øyvind: Well, we are close in 2.10 to a state where I am happy about how things are at the moment. It’s been a while since I was unhappy about howGIMP’s projection was driving the layer compositing code or creating a graph for compositing withGEGL– it’s been a long while since it was fixed. So when it comes to the performance of doing those things, or the performance on-canvas preview of vectors, the current problems are more inGEGLland thanGIMPland.

Jehan: InGEGL?

Øyvind: Yes, it’s an architectural puzzle to figure out, beforeGIMPshould change how it does its rendering to make use of the new capabilities inGEGL.

Jehan: So how fast canGEGLgo? How fast do you think (compared to now) it can improve?

Øyvind: I think for most filters in common use for photo manipulations as well as working with multiple layers, that even on aCPUthat you should have 10 frames per seconds updates on dragging layers around as well as doing color adjustment to the photos or the individual layers. I don’t see why that should be a big problem. That is what solving the mip-mapping problem should provide.

Debarshi Ray: Any plans for what you want to use forGEGL’sAPIdocumentation? It used to use kind of like GTKDoc at some point. There’s always the website, but any plans?

Øyvind: It currently displays a GObject introspection repository data directly on the website using Javascript. I kind of hope that the documentation people start working towards more documentation on GObject introspection and perhaps we align with something they do, if they do something like that.

Jehan: Do you want to seeGEGLin more software, not onlyGIMP?

Øyvind: That would be really nice because if people then create more filters and interesting things you can do in that software, it becomes available inGIMPand also in other software.

Jehan: Actually that’s very interesting. Can you explain a little about the architecture ofGEGLwhich makes it so that its filters can be available everywhere? How it will work in other software that integratesGEGL?

Øyvind: Well, you could imagine that for the operations you have inGIMPin terms of filters, there are many that you invoke for an image, that could be something that also you could apply as an effect in a video editor to a clip. You can animate some of the properties over time, like increasing or decreasing the blur on some background that you composite something on top of.

Michael Schumacher: What would you suggest people should do to learn about the capabilities ofGEGLand how to use it, either inGIMPdevelopment or in their own software?

Øyvind: Mostly, study what already exists, and if there is anything doing something similar to what they want already, then try to tweak that to do something new.

Michael Schumacher: Do you have a suggestion on what someone can use to play around withGEGL? For instance, if someone has fairly decent experience developing software, is there some kind of best approach like “Oh, use Python”?

Øyvind: I haven’t really tried to use any of the language bindings apart from C in a long while. I can see how approaching a library framework with C can be difficult for some users. But no, I don’t know of any of these integrated languages that have a very good integration.

Simon Budig: I think that the first start would be to use theGEGLcommand line tool and build trees inXMLor something like that.

Øyvind: I guess there’s also the data formats, theXMLandJSONbased data formats, as well as the data format you can fully construct on the command line just chaining operations and properties.

Debarshi Ray: Can you comment on howGEGLcompares to GStreamer, since they are both graph based and you can even do some image manipulation with GStreamer like their application does? Would it be easier withGEGL?

Øyvind:GEGLis focused on rendering and creating images. GStreamer is focused on playback and streaming of video. So the things passed around between the components of the graph of GStreamer are always full frames of videos. And it has many considerations for how to deal with playback and pre-feeding data to be able to stay in continuous playback and similar. WhereasGEGLhas only a concern about generating pixels for a static graph.

So the concerns involved in piecing together video codecs and the muxing of codecs and doing those things in a data flow, are different from doing just image processing with it – but kind of the core idea, which is visual programming using a graph instead of more like a human language with abstract syntax to create, is shared betweenGEGLand GStreamer. The data flow based approach and creating a framework for visual components and ordering.

Jehan: I have a similar question. There was an efficiency test – I think the product name was libvips – with various graphics software library, andGEGLwas in the list. In the tests they said it was worse.

Øyvind: Maybe that has improved recently, I’m not sure. BothGEGLand babl have had a traditional approach to bench-marking at runtime when things are already up and running and for interactive use. Whereas those benchmarks are based on equating command-line utilities with those that also include all the overhead of start-up. That is something that has improved recently in both, particularly in babl – it keeps measurement and profiling information from previous runs around in a file on disk so it can load, so it doesn’t have to do a lot of computations the first time you do a computation of a particular kind.

But I haven’t really re-run those benchmarks lately. But a lot of the trouble involved forGEGLand babl is that they’re very generic and have many plug-ins and do loads of file system access and those things before it can do any form of processing.

Jehan: Have you tried this libvips library?

Øyvind: Yes.

Jehan: How does it compare – not efficiency wise, butAPI, architecture? Why would one chooseGEGLover libvips?

Øyvind: That I don’t know. Depends on the capabilities of what you need it to do,GEGLis well on the way to have most traditionalGIMPfilters as operations. I haven’t studied the actual program APIs and how you would rig up pipelines with those APIs. I looked more at the graphical user interface of libvips – it’s an Excel spreadsheet-like approach to it, where you refer to data in a different cell. It’s one way of expressing a graph but I don’t know the actual programmatic APIs.

Jehan: So there’s different ways of expressing graphs?

Øyvind:GEGL’sAPIfor expressing and manipulating the graphs is loosely based on theW3C’s Document Object Model and hierarchical tree structures. I have no idea if or what type ofAPIinspirations that libvips is using.

Debarshi Ray: I have a question.GIMPhas a new website, shiny and everything. WillGEGLhave a new websiteas well?

Jehan: It has to be shiny!

Øyvind: Do you have aPNGfile called “Shiny” that we can use? Or do you also have someCSSand some pages and content for theGEGLwebsite?

Debarshi Ray: No, I have nothing.

Øyvind: I have tried for the last two or three years to make some existingGIMPandGEGLcontributors excited about writing some documentation and content as part of the website. They do rebuild the website every single time they buildGEGLand it ends up in the docs folder of the website. But it seems like it’s actually easier to get people to contribute code and new operations and exciting new features inGIMPand things than to get them to improve the website documentation.

And I must admit that I’d rather fix bugs and performance and features than spend too much time on the website.

Jehan: So, unless anyone has another question, we can finish…

Simon Budig: Did we talk about thePatreon?

Jehan: Oh right! So you’re trying to live off free software coding, especiallyGEGL. Can you try to explain it?

Øyvind: I spent a lot of time over the last ten years doing code for bothGEGLandGIMP, but also many other projects. It is strange how the media exploration experiments I do in code seem to not really have much cultural worth in society. So creating software and creating tools is not something that seems to be on the culture budget of any Western European country or something that would be considered part of improving the digital literacy of the population. It’s something that’s left up to private companies to maybe create software tools – but it’s not something that you’ll find on the budget of a country, that they want to let people improve and create tools for, say, image manipulation.

Maybe that’s a horrible way to start out to explain this.

Jehan: You can start over if you want.

Øyvind: I’ve been playing with creative expression in both visual media and in code for a couple of decades. I have made music videos, I’ve made short films, I’ve made paintings and I’ve made software. And sometimes when I make software, I get paid for it because there’s other business interests behind wanting it to exist. But I consider many of the contributions I’ve made toGIMPandGEGLto be valuable contributions, and that it would be good if I could do more of that type of experiments that end up in actual software – but also freely be able to do my own research and find out how it is possible to do a certain thing with videos or images or other ways that you can combine digital media types.

I’ve been fortunate enough to have had a software development job where I made a bit of money and had a safety cushion. So I’ve been living off savings for quite a while, creating software forGIMPand other things while traveling. But lately I’ve seen that my bank account has started screaming and turning red soon. So I was wondering, maybe this Patreon thing that I’ve seen both other software projects and other types of things suggested that I could try to keep bills paid. And I decided that okay, in some sense it’s asking for money and a little bit begging to be like a street music performer and saying “I’m making this thing and if you’re enjoying it, maybe you’d like me to continue doing some of the things I’m already doing”.

And it turns out there are a couple hundred people already who would like me to continue writing code and sharing it publicly and openly. That at least sustains me roughly on the level of unemployment benefits in European countries. And I hope that this will even slightly increase – I will not have a Silicon Valley level software developer salary, but I’ll have enough money to cover my expenses.

Øyvind’s portfolio website

Share this on:Mastodon|twitter|Facebook

Your Mastodon instance:
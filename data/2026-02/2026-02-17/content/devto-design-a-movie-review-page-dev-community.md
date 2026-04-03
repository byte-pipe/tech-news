---
title: Design a Movie Review Page - DEV Community
url: https://dev.to/richardpascoe/design-a-movie-review-page-36bl
site_name: devto
content_file: devto-design-a-movie-review-page-dev-community
fetched_at: '2026-02-17T11:20:05.900970'
original_url: https://dev.to/richardpascoe/design-a-movie-review-page-36bl
author: Richard Pascoe
date: '2026-02-10'
description: The next lab in the Accessibility section of the freeCodeCamp curriculum involves designing a Movie... Tagged with community, learning, programming, webdev.
tags: '#community, #learning, #programming, #webdev'
---

The next lab in the Accessibility section of the freeCodeCamp curriculum involves designing a Movie Review Page. As before, an example of the completed page is provided, along with the expected HTML boilerplate, which I've included below for reference:

<html

lang=
"en"
>


<head>


<meta

charset=
"UTF-8"
>


<meta

name=
"viewport"

content=
"width=device-width, initial-scale=1.0"
>


<title>
Movie Review
</title>


</head>

<body>

</body>

</html>

Enter fullscreen mode

Exit fullscreen mode

As with the previous labs, you'll need to complete the user stories and pass the required checks to move forward. The first story asks you to add a main element, and the second has you nest an h1 element for the movie title inside it.

These straightforward steps continue for the next couple of user stories, with an image added along with appropriate alt text, followed by a p element populated with a brief description of the movie. I didn't use the supplied image, to avoid my page looking like the example, so I sourced my own.

Another p element was then added to display the movie rating, which included a strong and span element, with the span using anaria-hiddenattribute.

The last few user stories involved adding an h2 element with a nested list. This list displayed the cast members, with their real names highlighted using the strong element. Once these steps were completed, the code passed and the lab was finished. You can see the completed code below, for clarity:

<!DOCTYPE html>

<html

lang=
"en"
>

<head>


<meta

charset=
"UTF-8"
>


<meta

name=
"viewport"

content=
"width=device-width, initial-scale=1.0"
>


<title>
Movie Review
</title>

</head>

<body>


<main>


<h1>
Logan's Run
</h1>


<img


src=
"https://bingeddata.s3.amazonaws.com/uploads/2020/12/logans-run-1.jpg"


height=
"480"


width=
"854"


alt=
"Still from Logan's Run (1976) showing the characters Logan and Jessica in a retro-futuristic city environment."


>


<p>


<em>
Logan's Run
</em>
 (1976) is a sci-fi film set in a dystopian future where society mandates that everyone must die at age 30.
 The story follows Logan, a "Sandman," who begins to question the system and goes on the run, uncovering the truth about his world.

</p>


<p>


<strong>
Movie Rating:
</strong>


<span

aria-hidden=
"true"
>
⭐⭐⭐⭐⭐⭐⭐⭐☆☆
</span>
(8/10)

</p>


<h2>
Cast Members
</h2>


<ul>


<li><strong>
Michael York
</strong>
 as Logan 5
</li>


<li><strong>
Jenny Agutter
</strong>
 as Jessica 6
</li>


<li><strong>
Richard Jordan
</strong>
 as Francis 7
</li>


<li><strong>
Roscoe Lee Browne
</strong>
 as Rem
</li>


<li><strong>
Farrah Fawcett
</strong>
 as Kris
</li>


<li><strong>
Peter Ustinov
</strong>
 as the Old Man
</li>


</ul>


</main>

</body>

</html>

Enter fullscreen mode

Exit fullscreen mode

With this lab successfully completed, only the third lab -Build a Multimedia Player- remains. I'll be sharing that lesson soon!

 The discussion has been locked. New comments can't be added.


 On hiatus. Comments closed for now.


For further actions, you may consider blocking this person and/orreporting abuse

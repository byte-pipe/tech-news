---
title: Component-based CSS - DEV Community
url: https://dev.to/moopet/component-based-css-4ic4
site_name: devto
content_file: devto-component-based-css-dev-community
fetched_at: '2026-04-09T11:24:57.174251'
original_url: https://dev.to/moopet/component-based-css-4ic4
author: Ben Sinclair
date: '2026-04-07'
description: There are a lot of CSS "solutions" out there. They generally act to solve a broad range of problems,... Tagged with css, ui, quickies.
tags: '#css, #ui, #quickies'
---

Scoped styling via native CSS nesting

There are a lot of CSS "solutions" out there. They generally act to solve a broad range of problems, none of which actually exist outside their authors' bubble.

Let me take you by the mitten and show you how I like to style components.

Here's "semantic-component-name.html":

<section
 
class=
"semantic-component-name-here"
>

 
<form>

 
<fieldset>

 
<legend>
Robin Hood
</legend>

 
<!-- etc... -->

 
</fieldset>

 
<fieldset>

 
<legend>
King Arthur
</legend>

 
<!-- etc... -->

 
</fieldset>

 
<input
 
type=
"submit"
 
value=
"Update history"
>

 
</form>

 
<p
 
class=
"disclaimer"
>

 None of these people are what you think they are.
 
</p>

</section>

Enter fullscreen mode

Exit fullscreen mode

and "semantic-component-name.css":

.semantic-component-name-here
 
{

/* Put everything in here... */

 
legend
 
{

 
color
:
 
var
(
--heading-color
);

 
font-size
:
 
1.5rem
;

 
}

 
.disclaimer
 
{

 
color
:
 
var
(
--ethically-dubious-color
,
 
#ccc
);

 
}

 
/* that's it. You're done. */

}

Enter fullscreen mode

Exit fullscreen mode

Your component, which has a distinct container class name, uses a semantic container tag, and inherits style variables from the parent theme... will just work.

You can update your look and feel from your global theme. You can use container queries to your heart's content. You can use tag selectors. They're all nested under the component's class, so they're not going to clash with anything.

You don't need to do anything special. You don't need to give every single element a generated random ID. You don't need to hard-code each component's padding inline with the tag, or define it in JavaScript. So put away that smelly CSS-in-JS. Stop importing stylesheets into React. Uninstall your preprocessors. You don't need any of that stuff.

Okay, you can aggregate and minimise the CSS. Don't purge anything though.

Don't remove unused CSS classes at build time. That's another solution to a problem that doesn't exist unless you literally design your code to BE the problem. And you don't do that, do you?

As a side-note, Svelte partially does this for you if you want to do React- or Vue-like things without having to run that sort of obsolete bloatware. Itdoesgive every component a random ID, but it's the closest to proper CSS handling I've seen outside of just doing it yourself in the first place.

Any questions?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
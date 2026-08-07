---
title: 5 best practices for preventing chaos in Tailwind CSS—Martian Chronicles, Evil Martians’ team blog
url: https://evilmartians.com/chronicles/5-best-practices-for-preventing-chaos-in-tailwind-css
site_name: tldr
content_file: tldr-5-best-practices-for-preventing-chaos-in-tailwind
fetched_at: '2026-08-07T19:52:02.955175'
original_url: https://evilmartians.com/chronicles/5-best-practices-for-preventing-chaos-in-tailwind-css
date: '2026-08-07'
published_date: '2026-08-05'
description: Tailwind CSS has become a very popular CSS framework, and it can speed up development. But using it without proper caution can add mayhem to your code. Learn best practices to avoid getting swept away!
tags:
- tldr
---

# 5 best practices for preventing chaos in Tailwind CSS

August 5, 2026
SKILL available

## Topics

* Tailwind CSS
* CSS
* JavaScript
* Nina TorgunakovaFrontend Engineer
* Travis TurnerTech Editor

## Translations

* KoreanTailwind CSS에서 혼란을 방지하기 위한 5가지 모범 사례
* JapaneseTailwind CSSをカオスにしないための5つのベストプラクティス

Working with Tailwind CSS is pretty fast and easy (that’s why it’s received such wide recognition). You just paste a list of different classes in your HTML—and your interface immediately becomes attractive! But, as the application grows, the lists of classes grow. Then, one day you realize you can’t understand your code, you’re confused with the structure of the application and magic variables, and work becomes a struggle. This article is all about avoiding this scenario, sharing some best practices to ensure you stay aloft when using Tailwind CSS.

Want your agent to do this for you?We packaged the guide as a skill you can download that includes every practice below, plus the anti-patterns to catch.

We can prevent headaches and resolve any problems (for the most part) by using Tailwind precisely and wisely. But, there are two requirements your project must meet, and if it doesn’t, Tailwind can actually make your job very difficult.

First, you should have a design system in your project. Tailwind’s philosophy couples with a design system where designers and developers use consistent design tokens. Design tokens are atomic values (like colors, spacing, or typography scales) that define a design’s properties and that are reused throughout the project.

Let’s imagine we have a standard button and some tabs that need to be the same color as that button:

.button
 
{

 
background-color
:
 
oklch
(
45
%
 
0.2
 
270
)
;

}

.tab
 
{

 
background-color
:
 
oklch
(
45
%
 
0.2
 
270
)
;

}

If we decide to change the color scheme of the project a little, we’ll need to find every instance of this color (which looks like a magic variable) and update them everywhere. This can be inconsistent and hard to maintain.

Irina NazarovaCEO at Evil Martians

We built open source projects PostCSS and Autoprefixer, used by millions of engineers. Hire us to optimize your frontend workflow and build scalable solutions.

Book a call

Design tokens help prevent these problems and ensure uniformity across UI elements.

Luckily, to implement design tokens, we only need to define them once—directly in your CSS via the@themedirective (or intailwind.config.jsif you still use Tailwind v3):

/* Tailwind v4 — your CSS entry file */

@theme
 
{

 
--color-primary
:
 
oklch
(
45
%
 
0.2
 
270
)
;

}

// Tailwind v3 — tailwind.config.js

module
.
exports
 
=
 
{

 
theme
:
 
{

 
colors
:
 
{

 
primary
:
 
"oklch(45% 0.2 270)"
,

 
}
,

 
}
,

}
;

After adding a new color with the nameprimary, we can usebg-primaryfor our background color ortext-primaryfor the text color throughout the application:

<
button
 
class
=
"
bg-primary
"
>
Standard button
</
button
>

<
div
 
class
=
"
bg-primary
"
>
First tab
</
div
>

This way, when you want to change the color scheme in the project, you only need to replace the color in one place.

It’s better toavoid using Tailwind if you haven’t considered a design systembecause you’ll have to write magic values in the class lists (like'p-[123px] mb-[11px] gap-[3px]') or add a lot of new tokens (15px,16px,17pxin the spacing config), and this will eventually bring a lot of mess to your code.

Having a consistent design system is good because it can help the development and design teams understand each other better.

For instance, within Figma, you can have a single shared source of truth for any values in your design system. But to make this system truly maintainable, you’ll need to introduce some conventions regarding token grouping and naming—which we’ll get into later in this article.

This is the second requirement your project needs to meet:you should already be using a component-based approach. The utility-first approach can lead to quite cluttered and verbose HTML structures since Tailwind classes apply directly to elements. This can mean the markup is harder to read and maintain, especially noticeable as your project grows.

The solution: actively using a component-based approach that encapsulates frequently used patterns (in our case, HTML elements appearing more than once) as separate components.

With this approach, we can keep thingsDRY. Moreover, we’ll still have a single source of truth for our Tailwind styles, and we can easily update it together in one place:

<
!
--
 
Reusable
 button 
with
 a long list 
of
 
Tailwind
 classes
:
 
--
>

<
button

 
class
=
"
bg-yellow-700 border-2 font-semibold border border-gray-300 text-green p-4 rounded
"

>

 Custom Button

</
button
>

<
!
--
 
Instead
 
of
 repeating 
this
 structure over and over again
,
 create a reusable component
:
 
--
>

<
CustomButton
>
Custom Button
</
CustomButton
>

If your development tool doesn’t allow you to split your code into components, it’s likely that the utility-first approach of Tailwind will only make development harder, and you should probably look to other CSS frameworks-for example,CSS Modules.

And one last thing regarding a component-based approach:avoid using the@applydirective:

.block
 
{

 
@apply
 bg-red-500 text-white p-4 rounded-lg 
active
:
bg-blue-700 
active
:
text-yellow-300 
hover
:
bg-blue-500 
hover
:
text-yellow-300
;

}

Yes, by using this directive, your code may look cleaner, but it throws away the key advantages of Tailwind: less mental overload when coming up with names for CSS classes, and the absence of regressions when changing styles (since with@applythey won’t be isolated within the component). Further, using it increases CSS bundle size.

In Tailwind v4,@applyalso needs an explicit@referenceimport to access your theme when used in a separately bundled stylesheet (CSS Modules, or a<style>block in Vue, Svelte, or Astro)—another reason to prefer CSS variables there instead.

If you met both requirements, Tailwind CSS is likely a good framework option for you! Here are the most helpful practices for improving your long-term experience with it.

## 1. Use fewer utility classes when possible

When you build a list of utility classes for an HTML element, each new class adds additional complexity for the developers, and they’ll have to analyze and work with the code later (and this includes you, too). Of course, these lists are an essential and inherent feature of Tailwind, but nevertheless, it’s better to write as little utility classes as possible.

Here are a few ways you can decrease the number of classes and get exactly the same results:

* Instead of settingpt-4pb-4, you can just usepy-4. This also applies with thepx,mx, andmyproperties.
* Instead offlex flex-row justify-between, you can just useflex justify-between. This is becauseflex-rowis the default value of theflex-directionproperty in CSS. In general, it can be valuable to remember some default values of other CSS properties (flex-wrap, for example) to make it easier to spot use cases like this.
* Instead of writing a long class list likeborder border-dotted border-2 border-black border-opacity-50, you can setborder-dotted border-2 border-black/50and this will have the same effect:border-2implies thatborderis set, andborder-black/50represents a shorthand for the RGBA format.

With a shorter list of classes, the next time you inspect the structure of your application, it’ll be much easier to analyze what’s going on.

## 2. Group design tokens and name them semantically

When working on a team, you probably agree that some clean coding practices (like the clear naming of variables) are really important for long-term development.

That said, even if you’re working alone, it also can be worth setting some rules for code clarity, otherwise, you could get confused about your own project (for example, when returning after a break).

This approach is especially important while working with Tailwind because reckless usage of such a large number of classes and design tokens can really bring confusion into your code.

As discussed above, using design tokens is a great practice, but just pasting them haphazardly can lead to chaos in your Tailwind configuration.

To remedy this, group related tokens together—in your@themeblock (v4) ortailwind.config.js(v3). This means that design tokens for breakpoints, colors, and so on, will be in specific areas and won’t mess with each other:

/* Tailwind v4 */

@theme
 
{

 
--color-primary
:
 
oklch
(
75
%
 
0.18
 
154
)
;

 
--color-secondary
:
 
oklch
(
40
%
 
0.23
 
283
)
;

 
--color-error
:
 
oklch
(
54
%
 
0.22
 
29
)
;

 
--spacing-sm
:
 
4
px
;

 
--spacing-md
:
 
8
px
;

 
--spacing-lg
:
 
12
px
;

 
--breakpoint-sm
:
 
640
px
;

 
--breakpoint-md
:
 
768
px
;

}

// Tailwind v3

module
.
exports
 
=
 
{

 
theme
:
 
{

 
colors
:
 
{

 
primary
:
 
"oklch(75% 0.18 154)"
,

 
secondary
:
 
"oklch(40% 0.23 283)"
,

 
error
:
 
"oklch(54% 0.22 29)"
,

 
}
,

 
spacing
:
 
{

 
sm
:
 
"4px"
,

 
md
:
 
"8px"
,

 
lg
:
 
"12px"
,

 
}
,

 
screens
:
 
{

 
sm
:
 
"640px"
,

 
md
:
 
"768px"
,

 
}
,

 
}
,

 
//...

}
;

Here’s another important thing: keeping a single semantic naming convention for your tokens will make it easier to find the necessary tokens and expand the system as the application grows.

For example, to add a color for your error state, don’t just copy and paste thebright-redtoken from your Figma file into your Tailwind configuration: put it into the colors section and give a more concise name likeerror. This will make the system much more consistent.

## 3. Keep class ordering

Here’s another clean coding convention: using a consistent order makes classes easier to read and understand. To illustrate, let’s take a look at some HTML elements with unsorted classes:

<
div
 
class
=
"
p-2 w-1/2 flex bg-black h-2 font-bold
"
>

 First block with unsorted classes

</
div
>

<
div
 
class
=
"
italic font-mono bg-white p-4 h-2 w-3 flex
"
>

 Second block with unsorted classes

</
div
>

In the blocks above, there are classes for different categories: dealing with the box model, display, typography, and so on—but they don’t have any sort of presentational order. We can apply a unified order to sort classes by categories:

<
div
 
class
=
"
flex h-2 w-1/2 bg-black p-2 font-bold
"
>

 First block with sorted classes

</
div
>

<
div
 
class
=
"
flex h-2 w-3 bg-white p-4 font-mono italic
"
>

 Second block with sorted classes

</
div
>

Since maintaining class ordering manually requires a lot of time and attention, it’s much better to automate this work usingthe official Prettier plugin for Tailwind CSS. To learn more about how to get started with it (and the methodology of how the classes are sorted), we recommend readingthis article.

## 4. Prevent inconsistencies when overriding and extending styles

Imagine that we use a component with a custom button on our page:

<
Button
 className
=
"bg-black"
 
/
>

And we have aButtoncomponent that has some default style:

export
 
const
 
Button
 
=
 
(
)
 
=>
 
{

 
return
 
<
button className
=
"bg-white"
>
Test
 button
<
/
button
>
;

}
;

In this case, the button will remain white since Tailwind doesn’t automatically override style and apply the black color, so we need to specify it in theButtoncomponent:

export
 
const
 
Button
 
=
 
(
{
 className 
=
 
"bg-white"
 
}
)
 
=>
 
{

 
return
 
<
button className
=
{
className
}
>
Test
 button
<
/
button
>
;

}
;

There’s nothing inherently wrong about this aspect of Tailwind, but if we want to customize some appearance by overriding or extending a lot of styles, it can be cumbersome to pass classes via props each time.

Moreover, there is one more drawback to this approach: accepting utilities via props can make it harder to ensure a consistent component view. This approach encourages using any utility combination for the same component across the app which can lead to a lack of visual consistency.

So, what can we do with it?

Instead of allowing any arbitrary utility classes to be passed via props, define a set of predefined variants:

const
 
BUTTON_VARIANTS
 
=
 
{

 
primary
:
 
"bg-blue-500 hover:bg-blue-600 text-white"
,

 
secondary
:
 
"bg-gray-500 hover:bg-gray-600 text-white"
,

 
danger
:
 
"bg-red-500 hover:bg-red-600 text-white"
,

}
;

Then, change theButtoncomponent so it can accept avariantprop. To make constructingclassNamemore convenient, you can useclsx:

export
 
const
 
Button
 
=
 
(
{
 className
,
 variant 
=
 
BUTTON_VARIANTS
.
primary
 
}
)
 
=>
 
{

 
return
 
<
button className
=
{
clsx
(
className
,
 variant
)
}
>
Test
 
Button
<
/
button
>
;

}
;

Tip: usingclsxwould be also especially handy if you need to construct classes conditionally.

After constructingclassNamefor the component, just use it, passing the desired variant:

<
Button
 variant
=
"secondary"
 
/
>

Now, consistency is ensured, and despite the fact that we added a restriction on full customization, flexibility remains; we can add any new variant for the component or edit an existing one.

And the other benefit of this approach is that it allows for simpler maintenance: changes to utility classes can be made in one place, and then propagated to every component of that variant in the app.

If for some reason you don’t want to use the sets of predefined variants, you can try the packagetailwind-merge, which provides utility functiontwMergeto merge Tailwind classes in JS without style conflicts. That said, it should be used carefully and only when necessary, since it is not the most lightweight and increases bundle size.

## 5. Minimize build size

Heavy CSS bundles mean slow-loading pages and frustrated users, so it’s worth making sure your production CSS is properly minified.

TL;DR:if you’re onTailwind v4, you don’t need to do anything—minification is automatic. If you’re onTailwind v3, you’ll need to set it up yourself.

### Tailwind v4: nothing to configure

Minification is handled automatically. Tailwind v4 is built on Lightning CSS, a Rust-based CSS parser and transformer, which handles parsing, vendor prefixing, and minification all in a single pass. This means you don’t need a separate minifier or autoprefixer in your build pipeline.

### Tailwind v3: set up minification

Minification removes all unnecessary characters (like whitespace, comments, and so on) and this will noticeably reduce file size.

Using the CLI, this can be done by setting the--minifyflag:

npx tailwindcss -o build.css --minify

If you’ve installed Tailwind as a PostCSS plugin instead, you can addcssnanoto your plugin list for minification.

If you don’t consider optimization, the size of your CSS can end up really big (more than several tens of kilobytes). Even in a small project with a few components with styles, there is a meaningful size difference after minifying CSS.

If you want to learn more about minification and compression for Tailwind v3,check this section of the documentation.

## Summing up: how to use (and how not to use) Tailwind

Tailwind is a powerful tool, but it’s important to use it while following some rules to prevent chaos from erupting in your project. Let’s sum up the above principles.

First, to get the most out of these practices, you should use Tailwind when you already have a design system and consistent design tokens and have opted for a component-based approach. Without breaking reusable elements into components, using Tailwind will become painful sooner or later, leading to repetitive or verbose HTML structures.

1. Minimize the number of utility classes where possible
2. Formulate code conventions within your team, for example, by grouping design tokens and naming them semantically
3. Likewise, implement consistent class ordering and set up linters to ensure code cleanliness
4. When appropriate, try to define a set of predefined variants for your components; this will help avoid problems with inconsistencies and style overriding
5. Minimize your bundle sizes: if you’re still on Tailwind v3, always minify the final CSS for your production build

By following these rules, you’ll be able to use Tailwind for the long haul, with pleasure and without problems, all while giving your team the chance to revel in all the benefits it provides.

Irina NazarovaCEO at Evil Martians

We built open source projects PostCSS and Autoprefixer, used by millions of engineers. Hire us to optimize your frontend workflow and build solutions that evolve with your developer tool's needs.

Book a call
Send email
 instead
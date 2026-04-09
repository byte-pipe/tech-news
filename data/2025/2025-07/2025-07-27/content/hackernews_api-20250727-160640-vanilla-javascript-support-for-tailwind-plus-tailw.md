---
title: Vanilla JavaScript support for Tailwind Plus - Tailwind CSS
url: https://tailwindcss.com/blog/vanilla-js-support-for-tailwind-plus
site_name: hackernews_api
fetched_at: '2025-07-27T16:06:40.749190'
original_url: https://tailwindcss.com/blog/vanilla-js-support-for-tailwind-plus
author: ulrischa
date: '2025-07-26'
description: Every UI block in Tailwind Plus is now fully functional, accessible, and interactive, even if you don't use a framework like React or Vue.
tags:
- hackernews
- trending
---

There are a lot of UI blocks in Tailwind Plus that need JavaScript to really be useful, like dialogs, dropdowns, command palettes, and more. And unless you're a React or Vue user, using those UI blocks has always meant writing all of that tricky JavaScript yourself.

Well today that finally changes —every UI block in Tailwind Plus is now fully functional, accessible, and interactive, including the plain HTML examples.

Now you can use anydropdown,command palette,dialog,drawer, and more in any project you're working on — no JavaScript framework required.

## No framework required

To pull this off, we built@tailwindplus/elements— a library we're releasing exclusively forTailwind Pluscustomers.

Elements is a collection of headlesscustom elementsthat wrap up all of the complex behavior needed to build custom interactive UIs using just HTML, and can be styled any way you like using utility classes or custom CSS.

Instead of being coupled to a specific JavaScript framework, these custom elements work anywhere you can use a<script>tag:

index.html
<
script
 src
=
"https://cdn.jsdelivr.net/npm/@tailwindplus/elements@1"
 type
=
"module"
></
script
>

Here's what it look like to build acustom dropdownmenu with Elements:

<
el-dropdown
 class
=
"relative inline-block text-left"
>
 <
button
 class
=
"inline-flex w-full justify-center gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-xs ring-1 ring-gray-300 ring-inset hover:bg-gray-50"
>
 Options
 <
svg
 viewBox
=
"0 0 20 20"
 fill
=
"currentColor"
 aria-hidden
=
"true"
 class
=
"-mr-1 size-5 text-gray-400"
>
 <
path
 d
=
"M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z"
 clip-rule
=
"evenodd"
 fill-rule
=
"evenodd"
 />
 </
svg
>
 </
button
>
 <
el-menu
 anchor
=
"bottom end"
 popover
 class
=
"w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black/5 transition transition-discrete [--anchor-gap:--spacing(2)] focus:outline-hidden data-closed:scale-95 data-closed:transform data-closed:opacity-0 data-enter:duration-100 data-enter:ease-out data-leave:duration-75 data-leave:ease-in"
>
 <
div
 class
=
"py-1"
>
 <
a
 href
=
"#"
 class
=
"block px-4 py-2 text-sm text-gray-700 focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden"
>
Account settings
</
a
>
 <
a
 href
=
"#"
 class
=
"block px-4 py-2 text-sm text-gray-700 focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden"
>
Support
</
a
>
 <
a
 href
=
"#"
 class
=
"block px-4 py-2 text-sm text-gray-700 focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden"
>
License
</
a
>
 <
form
 action
=
"#"
 method
=
"POST"
>
 <
button
 type
=
"submit"
 class
=
"block w-full px-4 py-2 text-left text-sm text-gray-700 focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden"
>
Sign out
</
button
>
 </
form
>
 </
div
>
 </
el-menu
>
</
el-dropdown
>

And here's what it looks like to build acustom select:

<
label
 for
=
"select"
 class
=
"block text-sm/6 font-medium text-gray-900"
>
Assigned to
</
label
>
<
el-select
 id
=
"select"
 name
=
"selected"
 value
=
"4"
 class
=
"mt-2 block"
>
 <
button
 type
=
"button"
 class
=
"grid w-full cursor-default grid-cols-1 ..."
>
 <
el-selectedcontent
></
el-selectedcontent
>
 <
svg
 viewBox
=
"0 0 16 16"
 fill
=
"currentColor"
 aria-hidden
=
"true"
 class
=
"col-start-1 row-start-1 ..."
>
 <!-- ... -->
 </
svg
>
 </
button
>
 <
el-options
 anchor
=
"bottom start"
 popover
 class
=
"max-h-60 w-(--button-width) [--anchor-gap:--spacing(1)] ..."
>
 <
el-option
 value
=
"1"
 class
=
"group/option relative block focus:bg-indigo-600 ..."
>
 <
div
 class
=
"flex items-center"
>
 <
span
 aria-hidden
=
"true"
 class
=
"inline-block size-2 shrink-0 ..."
></
span
>
 <
span
 class
=
"ml-3 block group-aria-selected/option:font-semibold ..."
>
 Wade Cooper
 <
span
 class
=
"sr-only"
>
 is online
</
span
>
 </
span
>
 </
div
>
 <
span
 class
=
"group-not-aria-selected/option:hidden group-focus/option:text-white in-[el-selectedcontent]:hidden ..."
>
 <
svg
 viewBox
=
"0 0 20 20"
 fill
=
"currentColor"
 aria-hidden
=
"true"
 class
=
"size-5"
>
 <!-- ... -->
 </
svg
>
 </
span
>
 </
el-option
>
 <!-- ... -->
 </
el-options
>
</
el-select
>

See those custom HTML elements like<el-select>and<el-options>? Those are the secret sauce that make everything work, including automatic ARIA attribute management, focus handling, keyboard support, and more.

You can even build something as sophisticated as a customcommand palettewith Elements, without having to write any of your own JavaScript:

<
button
 command
=
"show-modal"
 commandfor
=
"dialog"
 class
=
"rounded-md bg-white/80 px-2.5 py-1.5 text-sm font-semibold text-gray-900 hover:bg-white/90"
>
 Open command palette
</
button
>
<
el-dialog
>
 <
dialog
 id
=
"dialog"
 class
=
"backdrop:bg-transparent"
>
 <
el-dialog-backdrop
 class
=
"fixed inset-0 bg-gray-500/25 transition-opacity data-closed:opacity-0 data-enter:duration-300 data-enter:ease-out data-leave:duration-200 data-leave:ease-in"
></
div
>
 <
div
 tabindex
=
"0"
 class
=
"fixed inset-0 w-screen overflow-y-auto p-4 focus:outline-none sm:p-6 md:p-20"
>
 <
el-dialog-panel
 class
=
"mx-auto block max-w-3xl transform overflow-hidden rounded-xl bg-white shadow-2xl ring-1 ring-black/5 transition-all data-closed:scale-95 data-closed:opacity-0 data-enter:duration-300 data-enter:ease-out data-leave:duration-200 data-leave:ease-in"
>
 <
el-command-palette
 class
=
"divide-y divide-gray-100"
>
 <
div
 class
=
"grid grid-cols-1"
>
 <
input
 type
=
"text"
 autofocus
 placeholder
=
"Search..."
 class
=
"col-start-1 row-start-1 h-12 w-full pr-4 pl-11 text-base text-gray-900 outline-hidden placeholder:text-gray-400 sm:text-sm"
 />
 <
svg
 viewBox
=
"0 0 20 20"
 fill
=
"currentColor"
 aria-hidden
=
"true"
 class
=
"pointer-events-none col-start-1 row-start-1 ml-4 size-5 self-center text-gray-400"
>
 <
path
 d
=
"M9 3.5a5.5 5.5 0 1 0 0 11 5.5 5.5 0 0 0 0-11ZM2 9a7 7 0 1 1 12.452 4.391l3.328 3.329a.75.75 0 1 1-1.06 1.06l-3.329-3.328A7 7 0 0 1 2 9Z"
 clip-rule
=
"evenodd"
 fill-rule
=
"evenodd"
 />
 </
svg
>
 </
div
>
 <
div
 class
=
"flex transform-gpu divide-x divide-gray-100"
>
 <
div
 class
=
"max-h-96 min-w-0 flex-auto scroll-py-4 overflow-y-auto px-6 py-4"
>
 <
el-command-list
 class
=
"-mx-2 block text-sm text-gray-700"
>
 <
el-defaults
>
 <
h2
 class
=
"mx-2 mt-2 mb-4 text-xs font-semibold text-gray-500"
>
Recent searches
</
h2
>
 <
div
 class
=
"text-sm text-gray-700"
>
 <
a
 id
=
"person-suggestion-6"
 href
=
"#"
 class
=
"group flex cursor-default items-center rounded-md p-2 select-none focus:outline-hidden aria-selected:bg-gray-100 aria-selected:text-gray-900"
>
 <
img
 src
=
"https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
 alt
=
""
 class
=
"size-6 flex-none rounded-full"
 />
 <
span
 class
=
"ml-3 flex-auto truncate"
>
Tom Cook
</
span
>
 <
svg
 viewBox
=
"0 0 20 20"
 fill
=
"currentColor"
 aria-hidden
=
"true"
 class
=
"ml-3 hidden size-5 flex-none text-gray-400 group-aria-selected:block"
>
 <
path
 d
=
"M8.22 5.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.75.75 0 0 1-1.06-1.06L11.94 10 8.22 6.28a.75.75 0 0 1 0-1.06Z"
 clip-rule
=
"evenodd"
 fill-rule
=
"evenodd"
 />
 </
svg
>
 </
a
>
 <!-- ... -->
 </
div
>
 </
el-defaults
>
 <
el-command-group
 hidden
 class
=
"sm:h-96"
>
 <
a
 id
=
"person-1"
 href
=
"#"
 hidden
 class
=
"group flex cursor-default items-center rounded-md p-2 select-none focus:outline-hidden aria-selected:bg-gray-100 aria-selected:text-gray-900"
>
 <
img
 src
=
"https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
 alt
=
""
 class
=
"size-6 flex-none rounded-full"
 />
 <
span
 class
=
"ml-3 flex-auto truncate"
>
Leslie Alexander
</
span
>
 <
svg
 viewBox
=
"0 0 20 20"
 fill
=
"currentColor"
 aria-hidden
=
"true"
 class
=
"ml-3 hidden size-5 flex-none text-gray-400 group-aria-selected:block"
>
 <
path
 d
=
"M8.22 5.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.75.75 0 0 1-1.06-1.06L11.94 10 8.22 6.28a.75.75 0 0 1 0-1.06Z"
 clip-rule
=
"evenodd"
 fill-rule
=
"evenodd"
 />
 </
svg
>
 </
a
>
 <!-- ... -->
 </
el-command-group
>
 </
el-command-list
>
 <
el-no-results
 hidden
 class
=
"block px-6 py-14 text-center text-sm sm:px-14"
>
 <
svg
 viewBox
=
"0 0 24 24"
 fill
=
"none"
 stroke
=
"currentColor"
 stroke-width
=
"1.5"
 aria-hidden
=
"true"
 class
=
"mx-auto size-6 text-gray-400"
>
 <
path
 d
=
"M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z"
 stroke-linecap
=
"round"
 stroke-linejoin
=
"round"
 />
 </
svg
>
 <
p
 class
=
"mt-4 font-semibold text-gray-900"
>
No people found
</
p
>
 <
p
 class
=
"mt-2 text-gray-500"
>
We couldn't find anything with that term. Please try again.
</
p
>
 </
el-no-results
>
 </
div
>
 <
el-command-preview
 for
=
"person-1"
 hidden
 class
=
"h-96 w-1/2 flex-none flex-col divide-y divide-gray-100 overflow-y-auto sm:flex"
>
 <
div
 class
=
"flex-none p-6 text-center"
>
 <
img
 src
=
"https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
 alt
=
""
 class
=
"mx-auto size-16 rounded-full"
 />
 <
h2
 class
=
"mt-3 font-semibold text-gray-900"
>
Leslie Alexander
</
h2
>
 <
p
 class
=
"text-sm/6 text-gray-500"
>
Co-Founder / CEO
</
p
>
 </
div
>
 <
div
 class
=
"flex flex-auto flex-col justify-between p-6"
>
 <
dl
 class
=
"grid grid-cols-1 gap-x-6 gap-y-3 text-sm text-gray-700"
>
 <
dt
 class
=
"col-end-1 font-semibold text-gray-900"
>
Phone
</
dt
>
 <
dd
>
1-493-747-9031
</
dd
>
 <
dt
 class
=
"col-end-1 font-semibold text-gray-900"
>
URL
</
dt
>
 <
dd
 class
=
"truncate"
><
a
 href
=
"https://example.com"
 class
=
"text-indigo-600 underline"
>
https://example.com
</
a
></
dd
>
 <
dt
 class
=
"col-end-1 font-semibold text-gray-900"
>
Email
</
dt
>
 <
dd
 class
=
"truncate"
><
a
 href
=
"mailto:lesliealexander@example.com"
 class
=
"text-indigo-600 underline"
>
lesliealexander@example.com
</
a
></
dd
>
 </
dl
>
 <
button
 type
=
"button"
 class
=
"mt-6 w-full rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
>
Send message
</
button
>
 </
div
>
 </
el-command-preview
>
 <!-- ... -->
 </
div
>
 </
el-command-palette
>
 </
el-dialog-panel
>
 </
div
>
 </
dialog
>
</
el-dialog
>

To support all of the UI blocks in Tailwind Plus, we're shipping the following primitives in this first release of Elements:

* Autocomplete— for building things like customComboboxes.
* Command palette— for building customCommand Palettes.
* Dialog— for building customModal Dialogs,Drawers, and more.
* Disclosure— for building collapsibleFAQs, mobile menus inNavbars, and more.
* Dropdown menu— for building customDropdowns, of course.
* Popover— for building customFlyout Menusand more.
* Select— for building customSelect Menus.
* Tabs— for building custom tabs, like we use in customTextareasandProduct Overviews.

If you're a Tailwind Plus customer, head over to the brand newElements documentationto learn more about how everything works and check out some examples.

## Leveraging the modern web

We leaned on a lot of modern platform features to keep Elements as light and native as a possible.

* Custom elementsas a cross-platform component abstraction.
* Thepopoverattributeto manage overlays and popovers with automatic top-layer rendering together withbeforetoggleto control transitions.
* Native<dialog>elementsfor focus trapping and top-layer rendering.
* Invoker commandsto declaratively manage interactive elements, like toggling a custom disclosure.
* ElementInternalsto make our custom form controls work like native form controls.

We also bundle any necessary polyfills for these features to make sure that Elements works in all of the samebrowsers supported by Tailwind CSS v4.0. This means Elements will only get smaller as these modern platform features become more widely available.

## Components that work everywhere

Since HTML is the lowest common denominator between all web frameworks, Elements makes it possible for all of HTML-only UI blocks in Tailwind Plus to work literally anywhere.

Here's one of ourComboboxexamples wired up with two-way binding inSvelte:

Combobox.svelte
<
script
>
 let
 input
 =
 $state
(
""
)
;
 function
 handleSubmit
()
 {
 alert
(
`Selected:
${
input
}
`
)
;
 }
</
script
>
<
form
 onsubmit
=
{
handleSubmit
}
>
 <
label
 for
=
"autocomplete"
 class
=
"block text-sm/6 font-medium text-gray-900"
>
Assigned to
</
label
>
 <
el-autocomplete
 class
=
"relative mt-2 block"
>
 <
input
 bind:value
=
{input}
 id
=
"autocomplete"
 type
=
"text"
 class
=
"block w-full rounded-md ..."
 />
 <
button
 type
=
"button"
 class
=
"absolute inset-y-0 right-0 flex ..."
>
 <
svg
 viewBox
=
"0 0 20 20"
 fill
=
"currentColor"
 aria-hidden
=
"true"
 class
=
"size-5 text-gray-400"
>
 <
path
 d
=
"M5.22 8.22a.75.75 ..."
 clip-rule
=
"evenodd"
 fill-rule
=
"evenodd"
 />
 </
svg
>
 </
button
>
 <
el-options
 anchor
=
"bottom end"
 popover
 class
=
"max-h-60 w-(--input-width) [--anchor-gap:--spacing(1)] ..."
>
 <
el-option
 value
=
"Leslie Alexander"
 class
=
"block truncate aria-selected:bg-indigo-600 aria-selected:text-white ..."
>
Leslie Alexander
</
el-option
>
 </
el-options
>
 </
el-autocomplete
>
 <
button
 type
=
"submit"
>
Submit
</
button
>
</
form
>

Or here's a custom select inRailsthat's included in form submissions, just like a native form control:

app/controllers/orders_controller.rb
class
 OrdersController
 <
 ApplicationController
 def
 new
 @
cars
 =
 Car
.
all
 @
selected_car
 =
 @
cars
.
first
 end
 def
 create
 car
 =
Car
.
find
(
params
[:
car_id
])
 flash
[:
notice
]
 =
 "Selected car:
#{
car
.
name
}
"
 redirect_to root_path
 end
end
app/views/orders/new.html.erb
<%=
 form_with
do
 |
form
|
 %>
 <%=
 form
.
label
 :
car_id
,
 "Select model:"
 %>
 <
el-select
 name
=
"car_id"
 id
=
"car_id"
 value
=
"
<%=
 @
selected_car
.
id
 %>
"
>
 <
button
 type
=
"button"
 class
=
"grid w-full cursor-default grid-cols-1 ..."
>
 <
el-selectedcontent
 class
=
"col-start-1 row-start-1 truncate pr-6"
>
 <%=
 @
selected_car
.
name
 %>
 </
el-selectedcontent
>
 <
svg
 viewBox
=
"0 0 16 16"
 aria-hidden
=
"true"
 class
=
"col-start-1 row-start-1 size-5 ..."
>
 <
path
 d
=
"M5.22 10.22a.75.75 ..."
 clip-rule
=
"evenodd"
 fill-rule
=
"evenodd"
 />
 </
svg
>
 </
button
>
 <
el-options
 anchor
=
"bottom end"
 popover
=
""
>
 <%
 @
cars
.
each
 do
 |
car
|
 %>
 <
el-option
 value
=
"
<%=
 car
.
id
 %>
"
>
 <
span
 class
=
"block truncate font-normal group-aria-selected/option:font-semibold"
>
 <%=
 car
.
name
 %>
 </
span
>
 <
span
 class
=
"flex group-not-aria-selected/option:hidden group-focus/option:text-white in-[el-selectedcontent]:hidden ..."
>
 <
svg
 viewBox
=
"0 0 20 20"
 fill
=
"currentColor"
 aria-hidden
=
"true"
 class
=
"size-5"
>
 <
path
 d
=
"M16.704 4.153a.75.75 0 ..."
 clip-rule
=
"evenodd"
 fill-rule
=
"evenodd"
 />
 </
svg
>
 </
span
>
 </
el-option
>
 <%
 end
 %>
 </
el-options
>
 </
el-select
>
 <%=
 form
.
submit
 "Place order"
 %>
<%
 end
 %>

You can even use Elements inReactinstead of using a React-only library like Headless UI or React Aria if you want:

import
 Link
 from
 "next/link"
;
export
 function
 Menu
()
 {
 return
 (
 <
el-dropdown
 className
=
"relative inline-block text-left"
>
 <
button
 className
=
"inline-flex w-full justify-center ..."
>
 Menu
 <
svg
 viewBox
=
"0 0 20 20"
 fill
=
"currentColor"
 aria-hidden
=
"true"
 className
=
"-mr-1 size-5 text-gray-400"
>
 <
path
 d
=
"M5.22 8.22a.75.75 ..."
 clip-rule
=
"evenodd"
 fill-rule
=
"evenodd"
 />
 </
svg
>
 </
button
>
 <
el-menu
 anchor
=
"bottom end"
 popover
 className
=
"transition transition-discrete [--anchor-gap:--spacing(2)] focus:outline-hidden data-closed:scale-95 ..."
>
 <
div
 className
=
"py-1"
>
 <
Link
 href
=
"/"
 className
=
"block px-4 py-2 focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden ..."
>
Home
</
Link
>
 <
Link
 href
=
"/about"
 className
=
"block px-4 py-2 focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden ..."
>
About
</
Link
>
 <
Link
 href
=
"/faq"
 className
=
"block px-4 py-2 focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden ..."
>
FAQ
</
Link
>
 </
div
>
 </
el-menu
>
 </
el-dropdown
>
 )
;
}

## Try it out today

All of the updated UI blocks and the new Elements library are available now to allTailwind Pluscustomers.

Check out UI block categories likeDropdownsandCommand Palettesto play with these updated interactive examples yourself, and explore the newElements documentationto learn how it all works and how to customize things for your projects.

We can't wait to see what you'll build with this stuff!

---
title: 'Maple Mono: Open source monospace font'
url: https://font.subf.dev/en/
site_name: lobsters
content_file: lobsters-maple-mono-open-source-monospace-font
fetched_at: '2026-02-08T13:38:47.911071'
original_url: https://font.subf.dev/en/
date: '2026-02-08'
tags: design
---

# Maple Mono

Smooth your coding flow



We use code to bring ideas to life as products, but the font we choose is the silent architect that shapes how we experience that journey. Crafted for programmers,Maple Monoboosts your productivity with a subtle elegance, making every line of code a joy and smooth to read and write.



Learn More


Try it now







# Why Another One?





With so many excellent monospace fonts on the market, designed by professional designers and looking neat and beautiful, it’s surprising how many fall short when I actually use them for coding. I’ve found myself consistently dissatisfied with certain aspects, for example:

* JetBrains Monohas a refined glyph design and uniform layout, but its style feels a bit too rigid.
* Fira Codehas rich ligatures, but it lacks italics, and the automatically generated italic angle is too steep.
* Victor Monofeatures a cursive-style italic, but its slightly exaggerated style isn’t quite to my taste.
* Sarasa Gothicoffers a 2:1 monospace ratio for Chinese and English, but the English portion feels too narrow, impacting readability.
* Very few monospace fonts have rounded corners.
* Very few monospace fonts prioritize support forNerd-FontandChinese characters.

Therefore, I created this font with clean glyphs, a cursive-style italic, fine-grained configuration, built-inNerd-Font, and a 2:1 monospace ratio for Chinese and English. I create it to enhance my working experience, and hope that it can be useful to others.







# Features





## One Font, Infinite Weights



Variable font support, get whatever weight you like.




 V
 a
 r
 i
 a
 b
 l
 e






## Distinct Glyphs, Smooth Design



Round corners, brand-new glyph designs with cursive style in italic style.




@ $ &
% ->
cv01
Brand new glyphs with small gaps, disable it if you don't like it.
f i l
k x y
plain style
Cursive style of italic glyphs, allows fine-grain customization.
I 1 l
cv04
Distinct shapes for characters that are easy to confuse.
O 0 o
zero
Use slash style zero by default, instead of dot style.






## Smart Ligatures, Large Variety



Plain text tags, connected letters, brings the font capability to the next level.




Ligature ON
Ligature OFF
<>
a
??
b
!==
c
...
d
|->
<!--
e
++
f
!!
g
~>
h
</>
<=
i
###
j
:=
k
<==>
l
|>



### Special Ligatures



[DEBUG] [INFO] [WARN] [ERROR]
[TODO] todo)) [FIXME] fIxMe))
calt
Create tags from plain text, beautify your logs and tasks.


all class
ultra suffix
calt
Connected strokes in italic style, vivify your code.

1
>>
4
Vec<R<T
>>
calt
Smart spacing for generic (or template) and bitwise operations.







## Beautiful Icons, Embrace Modernity



First-class Nerd-Font support, iconize your modern terminal.






 Art By


CodeImg




 Theme


Maple




 Prompt


Starship









## Your favor, Your Font



{

 "
$schema
"
:
 "
./source/schema.json
"
,

 "
family_name
"
:
 "
Maple Mono
"
,

 "
use_hinted
"
:
 true
,

 "
pool_size
"
:
 4
,

 "
ligature
"
:
 true
,

 "
feature_freeze
"
:
 {

 // ...

 }

}



Configure or freeze OpenType features as you want, create your own perfect font.


See Guide




😡: "Why these glyphs are SOOOOO WEIRD ???"

 🤗: "Yeah I get that, so this one is for you:
Maple Mono Normal
 , a preset that reset all strange glyphs, make the glyph style similar to JetBrains Mono (with slashed 0). Direct download, no build required.

Enabled font features:

"cv01", "cv02", "cv33", "cv34", "cv35", "cv36", "cv61", "cv62", "ss05", "ss06", "ss07", "ss08"

 Preview
or

Test In Playground Page


class
 Example
 {

 private
 name
:
string
;

 @
Log

 public
 query
(
value
:
string
):
 void
 {

 const
 localVariable
 =
`
Hello,
${
this
.
name
}
! Query ->
${
value
}
`
;

 console
.
log
(
localVariable
,
 0x2312
)
;

 }

}







# Comparison



See how Maple Mono compares to other popular programming fonts.




JetBrains Mono
Fira Code
Iosevka
Italic
Cloudflare
Cloudflare






# Preview



See what the font looks like in real code snippets.





TypeScript JSX

function
 Counter
()
 {

 const
 [
val
,
 setVal
]
 =
 createSignal
(
10
)
;

 const
 dec
 =
 ()
 =>
 val
()
 !==
 ~~
3.1415926

 &&
 setVal
(
prev
 =>
 prev
--)
;

 return
 (

 <
button
 type
=
"
button
"
 onClick
={
dec
}>

 {
val
()}

 </
button
>

 )
;

}


Vue

<
script
 setup
>

import
 {
 ref
,
 computed
 }
 from
 '
vue
'

const
 count
=
 ref
(
0
)

const
 dbl
=
 computed
(()
 =>
 count
.
value
 *
 2
)

</
script
>

<
template
>

 {{
 dbl
 }}<
br
 />

 <
button
 @
click
=
"
count
++
"
>
Count
</
button
>

</
template
>


Java

@
SpringBootApplication

public
 class
 TodoApplication
 {

 public
 static
 void
 main
(
String
[]

args
)
 {

 SpringApplication
.
run
(
TodoApplication
.
class
,
 args
)
;

 Arrays
.
asList
(
"
foo
"
,
 "
bar
"
,
 "
baz
"
)

 .
stream
()

 .
map
(
String
::
toUpperCase
)

 .
forEach
(
System
.
out
::
println
)

 }

}


Go

func
 main
()
 {

 http
.
HandleFunc
(
"
/
"
,
 func
(
writer
 http
.
ResponseWriter
,
 request
 *
http
.
Request
)
 {

 message
 :=
 strings
.
Join
([]
string
{
"
Hello
"
,
 "
world!
"
},
 "
 "
)

 _
,
 err
 :=
 writer
.
Write
([]
byte
(
message
))

 if
 err
 !=
 nil
 {

 panic
(
err
)

 }

 })

 if
 err
 :=
 http
.
ListenAndServe
(
"
:8080
"
,
 nil
)
;
 err
 !=
 nil
 {

 panic
(
err
)

 }

}


Python

class
 Merger
(
object
):

 def
 merge
(
x1
,
 x2
):

 if
 isinstance
(
x1
,
 dict
)
 and
 isinstance
(
x2
,
 dict
)
:

 res
=
 x1
.
copy
()

 for
 k
,
 v
in
 x2
.
items
()
:

 res
[
k
]
 =
 merge
(
res
[
k
]
,
 v
)
 if
 k
in
 res
else
 v

 return
 res

 elif
 isinstance
(
x1
,
 list
)
 and
 isinstance
(
x2
,
 list
)
:

 res
=
 list
(
x1
)

 res
.
extend
(
x2
)

 return
 res

 else
:

 raise
 ValueError
(
f
"Cannot merge '
{
x1
!r
}
' and '
{
x2
!r
}
'"
)

if
 __main__
==
 "
main
"
:

 merger
=
 Merger
()

 merger
.
merge
(
0x23
,
 0xa1
)


C++

void
 quicksort
(
auto
 begin
,
 auto
 end
)
 {

 if
 (
begin
!=
 end
)
 {

 Comparable
auto
 pivot
=
 *
std
::
next
(
begin
,
 std
::
distance
(
begin
,
 end
)
 /
 2
)
;

 const
 auto
 [
lt
,
 gt
]
 =
 ::partition
(
begin
,
 end
,
 pivot
,
 std
::
less
<>())
;

 quicksort
(
begin
,
 lt
)
;

 quicksort
(
gt
,
 end
)
;

 }

}

int
 main
()
 {

 std
::
vector
<
int
>
 Vec
{
5
,
 0
,
 1
,
 5
,
 3
,
 7
,
 4
,
 2
}
;

 quicksort
(
Vec
.
begin
()
,
 Vec
.
end
())
;

 std
::
for_each
(

 Vec
.
begin
()
,

 Vec
.
end
()
,

 [](
const
 int
 Elem
)
 {
std
::
cout
<<
 Elem
<<
 "
 "
;
 }

 )
;

}







# What people say



Join thousands of developers who have already fallen in love with Maple Mono.




S
Siddharth Pant
Twitter
┏
Needed a font with some pazzazz🌟 and good italics. Maple Mono NF by @subframe7536 is my new favorite coding font. Just the font I was looking for after getting bored with JetBrains Mono. It takes inspiration from JBM and other great fonts
┛
T
TechEnthusiast
Discord
┏
Been using Maple Mono for a month now. The Nerd Font support is fantastic, and being able to customize font features is exactly what I needed. Great work!
┛
N
Nero
Twitter
┏
Having switched to the Maple Mono font and enabled italic ligatures for some parts, it feels a bit more lively on top of being clear and easy to use, which is nice.
┛
B
Beiyanyunyi
ZhiHu
┏
For those who prefer a rounder, more "adorable" font, Maple Mono might be a great choice. It includes CJK fonts and ensures a 2:1 width ratio. I've had about two or three colleagues compliment me on how good my editor and terminal look.
┛
E
ez_roma
Reddit
┏
I love Maple Mono because it is very similar to my handwriting. I write in a mixture of print and cursive so it feels like im looking at my handwriting. It also is very pleasing to look at the code with cursive flair instead of the more monotonous print.
┛






# Credits



Maple Mono is standing on the shoulders of giants.






 Base Font


JetBrains Mono







 Icon Integration


Nerd Fonts







 Port of CN glyphs


Resource Han Rounded







 Glyph Inspiration


Commit Mono

Fira Code

Iosevka

Monaspace

Monolisa

Recursive

Roboto Mono

Victor Mono







 Font Builder


Fonttools

FoundryTools-CLI

Pyodide







 Website Tools


Astro

SolidJS

UnoCSS

ESM.sh

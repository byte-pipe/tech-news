---
title: Yes, {} + [] = 0. No, JavaScript Isn’t Broken - DEV Community
url: https://dev.to/sylwia-lask/yes-0-no-javascript-isnt-broken-14ob
site_name: devto
content_file: devto-yes-0-no-javascript-isnt-broken-dev-community
fetched_at: '2026-10-30T12:47:27.237903'
original_url: https://dev.to/sylwia-lask/yes-0-no-javascript-isnt-broken-14ob
author: Sylwia Laskowska
date: '2026-10-29'
description: JavaScript is a legendary programming language. Created in the mid-1990s in just 10 days, it was born... Tagged with javascript, webdev, node, programming.
tags: '#javascript, #webdev, #node, #programming'
---

Born from airport boredom and spec quirks

JavaScript is a legendary programming language. Created in the mid-1990s in just 10 days, it was born during the browser wars, when Netscape was trying to deliver a fatal blow to Microsoft. As we all know, that didn't exactly work out as planned… Today, some people love JavaScript, others hate it, and some just make fun of it. But the truth is,the modern web simply wouldn't exist without it!

Over the years, JavaScript has gone through countless revolutions. Its capabilities today are almost incomparable to what the language could do back in the 1990s. There's just one tiny problem… Every change to the language has to take into account the fact that millions of websites out there still rely on old JavaScript behavior. And some of those websites will probably continue running that code until the end of time.

So, well,JavaScript's weirdness is probably here to stay forever!😂

After quite a long break, I've decided to bring back my once-popularJS WTFseries. For a very simple reason. I'm on my way back from iJS Munich, and I still have two hours to kill at Frankfurt Airport… (don't ask). Not enough time to write a groundbreaking, deeply technical article. But definitely too much time to just sit here and stare at the wall.

So let's take a look at one of my favorite JavaScript constructions:

{}
 
+
 
[]
 
// 0

Enter fullscreen mode

Exit fullscreen mode

Yes, you read that correctly. Under the right circumstances, if we add an empty object to an empty array in JavaScript, we get zero.And it makes perfect sense!🤡

## Wait, what? Why does this happen?

The first thing you need to know is thatJavaScript doesn't necessarily interpret{}as an object in this situation!Depending on the context, the JavaScript parser can treat the expression as two completely separate things.

Consider this code at the beginning of a statement in a classic JavaScript script:

{}
 
+
 
[]

Enter fullscreen mode

Exit fullscreen mode

JavaScript can interpret it like this:

{}
 
// An empty block of code

+
[]
 
// Unary plus applied to an empty array (what could go wrong?)

Enter fullscreen mode

Exit fullscreen mode

That's right. The first{}isn't an object literal at all. It's simply an empty block of code that does absolutely nothing. And the second part? Well, that's where the fun begins.

## The magic of type coercion ✨

The expression:

+
[]

Enter fullscreen mode

Exit fullscreen mode

is a classic example oftype coercion, one of the things our wonderful language is famous for.

As you probably know, JavaScript is a dynamically and weakly typed language.

Dynamic typing means that variables aren't permanently tied to one type. You can assign a number to a variable and then replace it with a string, and JavaScript won't complain.

But there's more! JavaScript also performs implicit type conversions, which is one of the reasons it's often described as weakly typed. And sometimes those conversions produce rather… creative results.

Take our unary plus operator:

+
[]

Enter fullscreen mode

Exit fullscreen mode

Unlike the binary+operator, which can add numbers or concatenate strings,unary plus tries to convert its operand into a numeric value.In this case, it behaves essentially like:

Number
([])

Enter fullscreen mode

Exit fullscreen mode

Yes, we're trying to convert an array into a number. Because why wouldn't we?

But before JavaScript can complete this operation, it needs to perform another conversion. An array is an object, and JavaScript first needs to obtain a primitive value from it. For an ordinary empty array, that process ends up calling itstoString()method.

And guess what?

[].
toString
();
 
// ""

Enter fullscreen mode

Exit fullscreen mode

An empty array becomes an empty string.

So our conversion effectively looks like this:

Number
([]);

// First, the array becomes a primitive string:

Number
(
""
);

// Then, the empty string becomes:

0

Enter fullscreen mode

Exit fullscreen mode

Because:

Number
(
""
)
 
// 0

Enter fullscreen mode

Exit fullscreen mode

And therefore:

+
[]
 
// 0

Enter fullscreen mode

Exit fullscreen mode

Which means our original construction:

{}
 
+
 
[]

Enter fullscreen mode

Exit fullscreen mode

when parsed as an empty block followed by unary plus, effectively becomes:

{}
 
// Do absolutely nothing

+
[]
 
// 0

Enter fullscreen mode

Exit fullscreen mode

And that's how we get zero!Simple and obvious, right? 🤡

To be fair, I can't think of another language where exactly this construction would produce such a perfectly normal-looking result. Even our beloved PHP would, I believe, throw a fatal error for something like this. Although PHP has its own collection of fascinating surprises, so perhaps we shouldn't judge too harshly.

One important detail:this behavior depends on how the code is parsed.For example:

// In a classic script, as a standalone statement:

{}
 
+
 
[]
 
// 0

// Force JavaScript to interpret {} as an object:

({}
 
+
 
[])
 
// "[object Object]"

// Inside a function call:

console
.
log
({}
 
+
 
[]);
 
// "[object Object]"

Enter fullscreen mode

Exit fullscreen mode

## Okay, but what about[] + []?

Now that you understand type coercion, this one should be obvious:

[]
 
+
 
[]
 
// ""

Enter fullscreen mode

Exit fullscreen mode

Here we're dealing with the binary+operator. JavaScript converts both arrays into primitive values. Well, what else would you expect when adding two empty strings together? 😀 Nothing plus nothing equals nothing! Beautiful.

## And now, apparently, addition isn't even commutative 😂

Following the same logic, let's try another expression:

[]
 
+
 
{}
 
// "[object Object]"

Enter fullscreen mode

Exit fullscreen mode

Wait a minute.

Didn't we just establish that:

{}
 
+
 
[]
 
// 0

Enter fullscreen mode

Exit fullscreen mode

So why does reversing the operands give us something completely different? Apparently, even the commutative property of addition is optional in JavaScript. xD

Well, technically, we're not always performing mathematical addition here, and the parser treats these expressions differently.

But let's not ruin a good joke with technical details. Here's what actually happens. In this expression:

[]
 
+
 
{}

Enter fullscreen mode

Exit fullscreen mode

The empty array becomes an empty string:

[].
toString
()
 
// ""

Enter fullscreen mode

Exit fullscreen mode

And the empty object? Well, a regular JavaScript object has its own wonderful string representation:

({}).
toString
()
 
// "[object Object]"

Enter fullscreen mode

Exit fullscreen mode

So JavaScript effectively performs:

""
 
+
 
"
[object Object]
"

Enter fullscreen mode

Exit fullscreen mode

Which gives us:

"
[object Object]
"

Enter fullscreen mode

Exit fullscreen mode

And that's it!Simple as building a flail.Okay, that's a literal translation of a Polish saying,proste jak budowa cepa, which means something is ridiculously easy to understand. And I think it fits JavaScript perfectly. 😂

## Final thoughts

I hope you enjoyed this little journey into the wonderful world of JavaScript weirdness. And I hope that after reading this article, you'll appreciate the beauty and originality of this magnificent language even more.

After all, JavaScript has been keeping us entertained for over 30 years, and I strongly suspect it has plenty of surprises left.

And the best part?None of the examples above are bugs.They're all consequences of JavaScript's parsing rules, type coercion, and the language's long history of backward compatibility. So next time someone tells you JavaScript is broken because{} + []can equal0, you can proudly explain why it makes perfect sense.

Next time I'll tell you why {} + {} = NaN... but unfortunately time flies when you're having fun, and I'll have to get ready for my flight soon!

P.S.If you enjoy my content, feel free to connect with me or leave a like onLinkedIn! ❤️

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
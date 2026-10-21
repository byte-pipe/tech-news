---
title: In Ruby, Objects Don't Have Methods. How Method Lookup Actually Works. - DEV Community
url: https://dev.to/smtahosin/in-ruby-objects-dont-have-methods-how-method-lookup-actually-works-31g9
site_name: devto
content_file: devto-in-ruby-objects-dont-have-methods-how-method-looku
fetched_at: '2026-10-21T15:51:36.779378'
original_url: https://dev.to/smtahosin/in-ruby-objects-dont-have-methods-how-method-lookup-actually-works-31g9
author: S M Tahosin
date: '2026-10-21'
description: A visual deep dive into Ruby's object model under the hood. Why objects store state but zero methods, how hidden eigenclasses work, and the real method lookup path. Tagged with ruby, programming, webdev, oop.
tags: '#ruby, #programming, #webdev, #oop'
---

Ask almost any developer how object-oriented programming works, and they will describe the same textbook picture: an object bundles data and methods together into a single unit.

In Ruby, you hear this idea reinforced constantly under the slogan:"Everything is an object."

You create a string, call.upcaseon it, and it feels completely natural to assume that the string object owns that method. You create a user object, call.save, and assume.savelives inside your user.

Except that is not how Ruby works at all.

In Ruby,objects contain zero methods.

If you inspect an instance down at the C source code level in CRuby (MRI), you discover something surprising: an object stores its instance variables, a set of internal flags, and a pointer to another structure. It does not contain a single line of method code, nor does it contain a method table.

Where do methods actually live? How does Ruby know what to execute when you typeuser.greet? And what actually happens when you define a method on a single specific object?

To truly master Ruby, you have to look beneath the syntactic sugar and understand the mechanics of Ruby's object model: method tables, the hiddeneigenclass, and the ancestry ladder.

## The First Surprise: Objects Store State, Classes Store Methods

Let us look at a simple Ruby class:

class
 
User

 
def
 
initialize
(
name
,
 
email
)

 
@name
 
=
 
name

 
@email
 
=
 
email

 
end

 
def
 
greet

 
"Hello, I am 
#{
@name
}
"

 
end

end

user
 
=
 
User
.
new
(
"Alice"
,
 
"alice@example.com"
)

Enter fullscreen mode

Exit fullscreen mode

When Ruby evaluatesUser.new, the virtual machine allocates a heap structure called anRObject.

Inside thisRObject, Ruby stores two things:

1. An array of instance variables:@nameset to"Alice", and@emailset to"alice@example.com".
2. An internal pointer namedklass, pointing directly to theUserclass object.

Notice what is missing fromuser:thegreetmethod is nowhere to be found.

Methods in Ruby live exclusively insideclasses(represented internally asRClass).

TheUserclass contains a hash table calledm_tbl(the method table). When you definedef greet, Ruby writes an entry intoUser's method table mapping the symbol:greetto its compiled bytecode body.

When you calluser.greet:

1. Ruby does not look insideuser.
2. Ruby followsuser's internalklasspointer to theUserclass.
3. Ruby searchesUser'sm_tblfor:greet.
4. It finds the method and executes it in the context ofself = user.

This separation is what makes Ruby memory-efficient. You can instantiate one hundred thousandUserobjects, and all one hundred thousand share the exact same method table insideUser. The instances only hold their personal instance variables.

## The Mystery of Singleton Methods

Now consider this famous Ruby feature: you can add a method to just one individual object without affecting any other instance of that class.

str1
 
=
 
"hello"

str2
 
=
 
"world"

def
 
str1
.
shout

 
upcase
 
+
 
"!!!"

end

str1
.
shout
 
#=> "HELLO!!!"

str2
.
shout
 
#=> NoMethodError: undefined method 'shout' for "world":String

Enter fullscreen mode

Exit fullscreen mode

This raises a fascinating puzzle:

* We already know that objects cannot hold methods. So:shoutcannot live insidestr1.
* :shoutcannot live insideString, because thenstr2would also have access to it.

If objects cannot hold methods, and the class cannot hold this method, where on earth doesshoutlive?

Ruby solves this by doing something brilliant:it quietly invents an invisible class on the fly.

The moment you define a method onstr1, Ruby creates an anonymous, hidden class called aneigenclass(officially referred to as asingleton class).

Ruby then performs an architectural sleight of hand:

1. It interceptsstr1's internalklasspointer and repoints it to this new singleton class (#<Class:str1>).
2. It sets the superclass of the singleton class toString.
3. It places the:shoutmethod inside the singleton class's method table.

When you callstr1.shout, Ruby follows theklasspointer into#<Class:str1>, finds:shout, and runs it.

When you callstr1.upcase, Ruby looks in#<Class:str1>, does not find:upcase, follows the superclass pointer up toString, finds:upcase, and runs it.

To regular code, the singleton class is almost completely transparent. You do not see it instr1.class(which still reportsString). But you can prove it exists with Ruby's reflection methods:

str1
.
singleton_class

#=> #<Class:#<String:0x00007fffa80c2180>>

str1
.
singleton_methods

#=> [:shout]

Enter fullscreen mode

Exit fullscreen mode

## "Class Methods" Do Not Exist

Once you understand eigenclasses, one of the biggest myths in Ruby evaporates:there is no such thing as a "class method".

Developers frequently write code like this:

class
 
Post

 
def
 
self
.
recent

 
# query recent posts

 
end

end

Enter fullscreen mode

Exit fullscreen mode

Tutorials often say:"This defines a class method on Post."

In languages like Java or C++, a static method is a distinct language construct. But in Ruby,Postis not a special entity.Postis simply an object.It is an instance of the classClass.

Post
.
class

#=> Class

Enter fullscreen mode

Exit fullscreen mode

BecausePostis an object, writingdef Post.recentordef self.recentis doing the exact same thing as writingdef str1.shout: it is defining asingleton methodon an object.

The:recentmethod does not live inPost, and it does not live inClass. It lives inPost's own private eigenclass (#<Class:Post>).

In Ruby, there are only instance methods. What we call "class methods" are merely instance methods living on the singleton class of a class object. The entire language operates on one single, unified rule.

## The Complete Method Lookup Ladder

When you typereceiver.message, what is the exact order Ruby follows to find the code?

Ruby does not search haphazardly. It walks an exact, deterministic ladder called theancestors chain. The first match it encounters executes immediately.

Here is the exact step-by-step lookup path:

1. The Receiver's Eigenclass:If the object has any singleton methods, they get first priority.
2. Prepended Modules on the Eigenclass:Any module added withprependsits in front of the eigenclass.
3. The Receiver's Class:The standard class where ordinary instance methods reside.
4. Prepended Modules on the Class:If a module wasprepended to the class, its methods override the class's own methods.
5. Included Modules on the Class:If a module wasincluded in the class, it is inserted directly above the class in the hierarchy.
6. Superclasses (and their modules):Ruby climbs to the parent class, checking its prepends, own methods, and includes.
7. Object, Kernel, and BasicObject:The root ancestors shared by virtually all Ruby objects.

### What Happens When Nothing Matches?

If Ruby climbs all the way toBasicObjectwithout finding a matching method, it does not immediately raise an error.

Instead, Ruby walks back down to the starting receiver and starts the entire search again from step one, this time searching for a method namedmethod_missing.

BecauseKernelprovides a default implementation ofmethod_missingthat raisesNoMethodError, your program only crashes if no intermediate module or class intercepts it.

This two-pass search is what powers Ruby's famous metaprogramming libraries, from ActiveRecord dynamic finders to OpenStruct.

## How "Everything Is an Object" Runs Fast: Tagged Pointers

If every number, boolean, and nil value in Ruby is an object with methods, how does Ruby avoid grinding to a halt allocating heap memory for basic math?

If you run:

total
 
=
 
0

1_000_000
.
times
 
{
 
|
i
|
 
total
 
+=
 
i
 
}

Enter fullscreen mode

Exit fullscreen mode

Does Ruby allocate one millionRObjectstructs on the heap?

In CRuby, the answer isno, thanks to an internal optimization calledTagged Pointers(Immediate Values).

On a 64-bit operating system, memory addresses are aligned to 8-byte boundaries. That means the lowest 3 bits of any valid heap pointer are always000.

CRuby takes advantage of these unused bits. When a 64-bit value represents a small integer (called aFixnum), Ruby shifts the integer left by one bit and sets the lowest bit to1:

value = (integer << 1) | 1

Enter fullscreen mode

Exit fullscreen mode

When the Ruby virtual machine sees a value with the lowest bit set to1, it knows:"This is not a heap pointer. This is the raw integer itself."

Similarly, CRuby reserves specific bit patterns for singleton values:

* falseis represented as0x00
* nilis represented as0x08
* trueis represented as0x14

When you call42.even?, Ruby does not inspect a heap block. It detects the tagged pointer, looks up the method in theIntegerclass method table, and executes the code without a single byte of memory allocation or garbage collection overhead.

You get the clean conceptual purity of "everything is an object" combined with the efficiency of primitive register arithmetic.

## The Mental Shift

Ruby's object model is often described as complex, but under the surface, it is remarkably minimal:

1. Objects store state and an internalklasspointer.They never hold methods.
2. Classes store methods and an internalsuperpointer.They never hold instance state.
3. Singleton methods live in invisible eigenclasses, seamlessly spliced into the lookup chain.
4. Class methods are just singleton methods on class objects, because classes are objects too.
5. Tagged pointers preserve pure object semanticswithout sacrificing performance.

Once you see the object model through this lens, Ruby metaprogramming stops feeling like black magic. Concepts likeclass_eval,instance_eval,prepend, and singleton classes become predictable mechanical tools that follow one coherent set of rules.

When you first learned Ruby, what was the quirk in its object model that made you stop and rethink how programming languages work? And if you have used eigenclasses in production, what was the problem you solved with them?

References:

* Ruby Core Documentation: Class and Object
* Ruby Core Documentation: Object#singleton_class
* Pat Shaughnessy: Ruby Under a Microscope(In-depth analysis of MRI C structures)
* Paolo Perrotta: Metaprogramming Ruby 2(The definitive guide to Ruby's object model)

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
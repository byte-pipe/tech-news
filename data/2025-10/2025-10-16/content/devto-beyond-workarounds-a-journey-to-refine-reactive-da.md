---
title: 'Beyond Workarounds: A Journey to Refine Reactive Data Models - DEV Community'
url: https://dev.to/tobi_augenstein/beyond-workarounds-a-journey-to-refine-reactive-data-models-3gdb
site_name: devto
fetched_at: '2025-10-16T11:08:23.128733'
original_url: https://dev.to/tobi_augenstein/beyond-workarounds-a-journey-to-refine-reactive-data-models-3gdb
author: Tobias Augenstein
date: '2025-10-14'
description: A long time ago, a small city in the beautiful South of Germany, an even smaller but innovative... Tagged with webdev, architecture, javascript, typescript.
tags: '#webdev, #architecture, #javascript, #typescript'
---

A long time ago, a small city in the beautiful South of Germany, an even smaller but innovative software company - that's where this journey started.

## First Encounter

The company I worked for specialized in low-code business process automation. I had just been promoted to lead frontend product development and was in charge ofcreating a visual UI builder that would seamlessly integrate with the existing product ecosystem. Initially we thought building a custom reactivity system for dynamic UIs wouldn’t make sense - obviously we should build on top of something proven and stable rather than reinventing the wheel, right?

Back thenKnockout seemed like a good choiceand it worked well at the beginning.Butover time,the more we built on top, the more we had towork around default behaviorof the framework and ran intoperformance, stability and maintainability issues. At some point I figured it would be easier to replace it with a custom foundation that really fit our needs instead of continuing to add more workarounds. Eventually we developed a simple specialized core API and afterwards it actually worked fast and reliable with minimal maintenance.

## History Repeats

Later in my career I was involved in building other complex products based onAngular and Vue. The experience with both of them was not much different. They work okay for standard web projects, butwhen you build highly-configurable products on top it becomes painful. The new APIs in Vue 3 and Signals in Angular finally support more flexibility and control, but working with them is still not really convenient from my perspective.

One of my IT teachers in high school once said: A good developer needs to be lazy. I took that to heart. :)I'm too lazy topass around additional meta-contextall the time because the data model has no idea about itself. Too lazy toalways explicitly initialize nested objectsbefore access. Too lazy tomap data to a different data-structure to do basic operations efficiently. I also don’t want toseparately manage state tracking for validation and loading. And I don't wantbroken reactivitythat’s a nightmare to debug because something was not created or tracked at the right time or in the right context.But how can these issues be avoided? My go-to solution has been custom data wrappers.

## Applied Lessons

While repeatedly buildingwrappersand proxiesaround reactive data, I noticed recurring patterns. In the following sub-chapters we'll have a look at some of the most useful concepts. The code examples use implementations with plain values thatcan be adapted across frameworks(just replace the plain fields with reactive references like Vue Refs, Angular Signals, etc.). Later implementations extend previous ones and focus on relevant new aspects to keep things tidy.

### Implicit Initialization

In nested object structures it can be quite tiresome and error prone to always make sure objects are initialized before accessing properties. Modern JS features and TS help, but it’s still not convenient. A custom wrapper that dynamically accesses properties can simplify that.

Plain optional initialization:

data
.
users

??=

{};

data
.
users
[
userId
]

??=

{};

const

user

=

data
.
users
[
userId
];

user
.
contact

??=

{};

user
.
contact
.
email

=

email
;

user
.
location

??=

{};

user
.
location
.
address

=

address
;

Enter fullscreen mode

Exit fullscreen mode

Wrapper with implicit initialization:

const

user

=

model
.
prop
(
'
users
'
).
prop
(
userId
);

user
.
prop
(
'
contact
'
).
prop
(
'
email
'
).
set
(
email
);

user
.
prop
(
'
location
'
).
prop
(
'
address
'
).
set
(
address
);

Enter fullscreen mode

Exit fullscreen mode

With TS we can ensure that dynamic keys only support valid properties and that the child model inherits the correct type. Here’s a basic version of theprop()method.

prop
<
K

extends

keyof

T
>
(
key
:

K
):

Model
<
T
[
K
]
>

{


let

prop

=

this
.
props
.
get
(
key
)

as

Model
<
T
[
K
]
>
;


if
(
!
prop
)

{


prop

=

new

Model
();


this
.
props
.
set
(
key
,

prop
);


}


return

prop
;

}

Enter fullscreen mode

Exit fullscreen mode

Simplified initialization is nice, but the real value of this model approach shows when things get more complex. So let's move on to more advanced concepts.

### Context-Awareness

Ever had this issue: You pass data to a function or child component and later you need the key or index of that data? Or you want to remove data but can’t do that without access to its parent. Sure, you can pass down the key, index, parent or whatever else you need. If it’s just one level that’s not a big deal, but in complex applications it can become very messy. Wouldn’t it be great if the data model just had this context information available?

This is how an example could look:

function

performAction
(
user
:

Model
<
User
>
,

action
:

UserAction
):

boolean

{


console
.
log
(
'
Perform action for user
'
,

user
.
key
,

'
:
'
,

action
);


switch
(
action
)

{


case

'
duplicate
'
:


return

duplicateProp
(
user
,

createId
());


case

'
remove
'
:


return

user
.
remove
();


default
:


throw

new

Error
(
`Unknown action:
${
action
}
`
);


}

}

Enter fullscreen mode

Exit fullscreen mode

duplicateProp functionfunctionduplicateProp<T>(prop:Model<T>,newKey:string):boolean{constparent=prop.parentasModel<Record<string,T>>|undefined;if(parent){parent.prop(newKey).set(prop.get());returntrue;}returnfalse;}Enter fullscreen modeExit fullscreen modeHere’s a basic outline of the implementation (see full class in the collapsible below).

class

Model
<
T
>

{


readonly

key
?:

string
;


readonly

parent
?:

Model
<
unknown
>
;


// ...


remove
():

boolean

{


const

props

=

this
.
parent
?.
props
;


if
(
props

&&

this
.
key
)

{


return

props
.
delete
(
this
.
key
);


}


return

false
;


}

}

Enter fullscreen mode

Exit fullscreen mode

Full Model classtypeKeyOf<T>=keyofT&string;typePropOf<T>=T[KeyOf<T>];classModel<T>{protectedprops?:Map<string,Model<unknown>>;protectedvalue?:T;// replace with reactive referenceconstructor(data?:T,readonlykey?:string,readonlyparent?:Model<unknown>){this.set(data);}get():Partial<T>|undefined{if(!this.props){returnthis.value;}constdata:Partial<T>={};for(const[key,prop]ofthis.props){data[keyasKeyOf<T>]=prop.get()asPropOf<T>;}returndata;}set(data?:Partial<T>):void{if(typeofdata==='object'&&data!==null){this.clear();for(const[key,value]ofObject.entries(data)){this.prop(keyasKeyOf<T>).set(valueasPropOf<T>);}}else{this.value=data;this.props=undefined;}}clear():void{this.value=undefined;this.props?.forEach(prop=>prop.clear());}prop<KextendsKeyOf<T>>(key:K):Model<T[K]>{this.props??=newMap();letprop=this.props.get(key)asModel<T[K]>;if(!prop){prop=newModel<T[K]>(undefined,key,this);this.props.set(key,prop);}returnprop;}remove():boolean{constprops=this.parent?.props;if(props&&this.key){returnprops.delete(this.key);}returnfalse;}}Enter fullscreen modeExit fullscreen mode

### Consistent Access & Iteration

Another recurring challenge is deciding whether to store a collection as an array or a map. At first it seems easy - arrays for lists and maps for key-based lookup. But in many real-world cases you need both and then it gets complicated. A model that supports both internally and transparently keeps them in sync can be very useful for those cases.

const

model

=

new

Model
({
a
:

true
,

b
:

false
,

c
:

null
});

log
(
model
.
prop
(
'
b
'
).
index
);

// → 1

log
(
model
.
item
(
1
).
key
);

// → b

log
(
model
.
child
(
'
b
'
)

===

model
.
child
(
1
));

// → true

model
.
forEach
(
child

=>

log
(
child
.
index
,

child
.
key
,

child
.
get
()));

// → 0 a true / 1 b false / 2 c null

Enter fullscreen mode

Exit fullscreen mode

If the base structure is a list, the model can automatically generate keys to allow the same kind of dual access. Let's dive deeper into that!

### Stable (Deep) References

Using indexes for referencing list items can easily become inconsistent when the list changes. And using an ID to identify items leads to inefficient search in the list. With our combined model approach and generated keys, a stable and efficient lookup is fairly simple.

class

ListSelection
<
Item
>

{


protected

key
?:

string
;

// replace with reactive reference


constructor
(
readonly

list
:

Model
<
Item
[]
>
)

{


}


get

selected
():

Model
<
Item
>

|

undefined

{


const

{
key
}

=

this
;


return

key

?

this
.
list
.
child
(
key
)

:

undefined
;


}


select
(
index
:

number
):

void

{


this
.
key

=

this
.
list
.
item
(
index
).
key
;


}

}

Enter fullscreen mode

Exit fullscreen mode

And the implementation is also quite straightforward, although it should have better key/index validation than the following minimalistic example.List Access Impl.typeItemOf<T>=TextendsArray<any>?T[number]:unknown;classModel<T>{// ...#items?:Model<ItemOf<T>>[];protectedgetitems():Model<ItemOf<T>>[]{return(this.#items??=[]);}getindex():number|undefined{// for better performance, cache the index when creating the item// and update or mark as dirty when the list changesreturnthis.parent?.items.indexOf(this);}child(key:string|number):Model<ItemOf<T>>{if(typeofkey==='string'){returnthis.prop(keyasKeyOf<T>)asModel<ItemOf<T>>;}returnthis.item(key);}item(index:number):Model<ItemOf<T>>{if(index<this.items.length){returnthis.items[index];}returnthis.add();}add(data?:ItemOf<T>):Model<ItemOf<T>>{returnthis.insert(this.items.length,data);}insert(index:number,data?:ItemOf<T>):Model<ItemOf<T>>{constkey=this.createKey();// creates a unique item keyconstitem=newModel(data,key,this);this.items.splice(index,0,item);this.props.set(key,item);returnitem;}}Enter fullscreen modeExit fullscreen modeNow we have stable references for items of flat lists, but what if we have deep nested data structures and want to reference any entry there? With a few little extensions we can cover that too.

const

node

=

tree
.
prop
(
'
nodes
'
).
item
(
3
).
prop
(
'
nodes
'
).
item
(
2
);

const

ref

=

node
.
ref
;

// stable deep reference

log
(
tree
.
resolve
(
ref
)

===

node
);

// → true

log
(
node
.
resolve
(
ref
)

===

node
);

// → true

log
(
node
.
resolve
(
SpecialKeys
.
root
)

===

tree
);

// → true

log
(
node
.
resolve
(
SpecialKeys
.
parent
)

===

node
.
parent
);

// → true

Enter fullscreen mode

Exit fullscreen mode

This provides us with a powerful way to reference any other entry within the same model hierarchy by relative or absolute (root-based) references. And the implementation for that is also no rocket science.Deep Reference Impl.classModel<T>{// ...getroot():Model<unknown>{returnthis.parent?.root||this;}getref():string{constbase=this.parent?.ref||SpecialKeys.root;returnthis.key?`${base}.${this.key}`:base;}resolve(ref:string):Model<unknown>|undefined{letmodel:Model<unknown>|undefined=this;for(constkeyofref.split('.')){model=model?.access(key);}returnmodel;}}access(key?:SpecialKeys|string|number):Model<unknown>|undefined{if(!key)returnthis;switch(key){caseSpecialKeys.root:returnthis.root;caseSpecialKeys.parent:returnthis.parent;default:returnthis.child(key);}}Enter fullscreen modeExit fullscreen mode

### Internal Validation & Loading State

In most applications we need to be able to check whether data is currently loading and if changed data is valid. Logically, both of these state information are closely tied to the data - including them directly into the data model avoids inconsistencies and helps to keep the code simple.

submitTask
(
task
:

Model
<
Task
>
):

void

{


if
(
task
.
isValid

&&

!
task
.
isLoading
)

{


// ...


}

}

Enter fullscreen mode

Exit fullscreen mode

The following code snippet shows a simple example for loading state integration.Simple Loading StateexportclassModel<T>{// ...protectedloading=0;// replace with reactive referencegetisLoading():boolean{return!!this.loading;}asyncupdateAsync(promise:Promise<T|undefined>):Promise<boolean>{this.loading++;try{constdata=awaitpromise;this.set(data);returntrue;}catch(e){// add error handlingreturnfalse;}finally{this.loading--;}}}Enter fullscreen modeExit fullscreen modeDepending on the context, you may want to use external libraries or track additional meta information, especially for validation. In the next chapter we will explore more advanced patterns to track different kinds of async state simple and reliable.

### Generic Async State Management

For simple cases a boolean flag, status type or counter can be enough to track the state of async operations. But often we need more detailed state information, for example error messages. Plus we also want to be able to cancel pending operations and avoid race conditions. The following implementations solve those issues with a lightweight, unified wrapper class.LoadingclassModel<T>{// ...#request?:DynamicState;getrequest():DynamicState{return(this.#request??=newDynamicState());}getisLoading():boolean{returnthis.request.isPending;}asyncupdateAsync(promise:Promise<T|undefined>):Promise<boolean>{constupdate=this.request.update();try{constdata=awaitpromise;returnupdate.ready(()=>this.set(data));}catch(e){console.error(e);update.fail('Request failed');returnfalse;}}}Enter fullscreen modeExit fullscreen modeValidationclassModel<T>{// ...#validation?:DynamicState;getvalidation():DynamicState{return(this.#validation??=newDynamicState());}getisValid():boolean{returnthis.validation.isSuccess;}asyncvalidate(check:(model:Model<T>)=>Promise<string|undefined>):Promise<boolean>{constvalidation=this.validation.update();consterrorMsg=awaitcheck(this);if(errorMsg){validation.fail(errorMsg);returnfalse;}returnvalidation.ready();}}Enter fullscreen modeExit fullscreen modeDynamic StatetypeStateValue='pending'|'success'|'failed'|'canceled';classStateUpdate{constructor(protected_ready?:(state:StateValue,message?:string)=>void){}ready(success?:()=>void,message?:string):boolean{if(this._ready){success?.();this._ready('success',message);returntrue;}returnfalse;}fail(message?:string):void{this._ready?.('failed',message);this.destroy();}cancel():void{this._ready?.('canceled');this.destroy();}destroy():void{this._ready=undefined;}}classDynamicState{#state?:StateValue;// replace with reactive reference#message?:string;// replace with reactive reference#update?:StateUpdate;getisInitial():boolean{return!this.#state;}getisPending():boolean{returnthis.#state==='pending';}getisSuccess():boolean{returnthis.#state==='success';}getisFailed():boolean{returnthis.#state==='failed';}getisReady():boolean{returnthis.isSuccess||this.isFailed;}getmessage():string|undefined{returnthis.#message;}update():StateUpdate{this.#state='pending';this.#update?.destroy();this.#update=newStateUpdate((state,message)=>{this.#state=state;this.#message=message;});returnthis.#update;}}Enter fullscreen modeExit fullscreen mode

## Beyond Wrappers

As we have seen, many useful data model features can be realized by just wrapping reactive values of common frameworks. This approach can add convenience and help to maintain cleaner code, but it can’t overcome deeper limitations. Handling edge cases efficiently and reliably also becomes tricky. Let’s look at two more fundamental issues I’ve struggled with and concepts to address them.

### Explicit Dependency Tracking

Sometimes there is side-effect logic within the code that’s executed by reactive bindings. If that logic accesses reactive data, a change of this data will also trigger an update, even though it’s not meant to be a dependency. Angular, for example, introduced anuntrackedfunction as part of Signals to avoid unwanted tracking. Explicit tracking inverts that approach, enablesmore flexible controland makes itmore transparentwhich parts of an application depend on reactive values.

More importantly, itseamlessly works with async logic. Modern front-ends rely a lot on async logic, but reactive state tracking usually requires sync execution of dependencies. That means, all reactive values need to be resolved outside of async code and then be passed down through async call hierarchies, which limits architecture options and can easily lead to significantly more complex FE structures. Explicit dependency trackingprovides more architectural freedomand, for example, enables us to organize main structures more in an OOP style. But it requires a fundamentally different approach to reactivity and can’t be done by just adding a wrapper for sync reactive systems.

Here’s a separate article on how it can be a game-changer for async reactive logic, in case you want to dive deeper:

## An Explicit Approach to Async Reactivity

### Tobias Augenstein ・ Sep 4

#webdev

#javascript

#typescript

#architecture

### Language-Agnostic Full-Stack Models

A big annoyance in full-stack applications is managingconsistent data models between FE and BE. One solution is using JS for BE, but that’s not an option in many contexts for good reasons - while there have been many improvements, it’s still not well suited for building reliable and scalable business logic. The Google Web Toolkit tried another interesting approach to use a common language, but using Java for FE was too complex. And in general I don’t think it’s a good idea to become limited to one specific language. To me, the best solution for this issue seems to be adeclarative abstraction layer that defines data structures and high-level validation logic. Standards like OpenAPI and GraphQL enable shared schemas, but they don’t support shared logic for computed data and advanced validation. I’d like to have a unified full-stack solution that defines data structures and their related logic in a consistent way. When such structures are based on a common format like JSON, it’s relatively easy to build interpreters in most major languages, which can provide a lot of technological flexibility. That’s what the next step of my journey is aimed at.

## A New Foundation

Throughout my career I have come across all the above issues repeatedly and developed multiple solutions for most of them. EventuallyI became tired of solving the same things over and over again, so I started to create one framework to solve them all. :)

If you want to learn more about it, here’s an overview on the general concepts:

## Bridging the Gap: Low-Code for Web Developers

### Tobias Augenstein ・ Mar 5

#webdev

#lowcode

#nocode

#architecture

## And Now?

Now you wait until my framework is released and all struggles will be gone! 😁

Jokes aside, of course these concepts don’t solve all issues with data models and obviously they also come with trade-offs. But I hope they can provide some help to work more efficiently with reactive data.

And if you’re interested to see my framework’s prototype in action or follow the further development, check out the website:https://ontineo.com

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

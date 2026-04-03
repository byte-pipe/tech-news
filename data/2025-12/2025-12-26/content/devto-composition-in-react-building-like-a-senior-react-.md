---
title: 'Composition in React: Building like a Senior React Dev - DEV Community'
url: https://dev.to/emann/compound-components-in-react-building-like-a-senior-react-dev-56dm
site_name: devto
fetched_at: '2025-12-26T19:06:38.520480'
original_url: https://dev.to/emann/compound-components-in-react-building-like-a-senior-react-dev-56dm
author: Emmanuel Sunday
date: '2025-12-20'
description: Raise your hand if you've ever worked with an external UI library. ✋. I'm a big fan of Shadcn... Tagged with webdev, react, architecture, typescript.
tags: '#webdev, #react, #architecture, #typescript'
---

Raise your hand if you've ever worked with an external UI library.

✋.

I'm a big fan of Shadcn myself.

These are the heroes front-end devs didn't ask for but need dearly.

Beautiful UIs. Quick Implementations.

Beautiful stuff.

But that's actually not the point of discussion.

Walk with me, let's do some analysis with these libraries.

## React Composition

Assuming I wanted to work with a library like Shadcn, and chose to use the card components for whatever reason.

It's straightforward.

pnpm add shadcn@latest card

Enter fullscreen mode

Exit fullscreen mode

Now, how do I use this card component?

export

function

Card
()

{


return
(


<
Card

className
=
"w-full max-w-sm"
>


<
CardHeader
>


<
CardTitle
>
Login to your account
</
CardTitle
>


<
CardDescription
>

 Enter your email below to log in to your account

</
CardDescription
>


<
CardAction
>


<
Button

variant
=
"link"
>
Sign Up
</
Button
>


</
CardAction
>


</
CardHeader
>


<
CardContent
>


<
form
>


<
div

className
=
"flex flex-col gap-6"
>


<
div

className
=
"grid gap-2"
>


<
Label

htmlFor
=
"email"
>
Email
</
Label
>


<
Input


id
=
"email"


type
=
"email"


placeholder
=
"m@example.com"


required


/>


</
div
>


<
div

className
=
"grid gap-2"
>


<
div

className
=
"flex items-center"
>


<
Label

htmlFor
=
"password"
>
Password
</
Label
>


<
a


href
=
"#"


className
=
"ml-auto inline-block text-sm underline-offset-4 hover:underline"


>

 Forgot your password?

</
a
>


</
div
>


<
Input

id
=
"password"

type
=
"password"

required

/>


</
div
>


</
div
>


</
form
>


</
CardContent
>


<
CardFooter

className
=
"flex-col gap-2"
>


<
Button

type
=
"submit"

className
=
"w-full"
>

 Login

</
Button
>


<
Button

variant
=
"outline"

className
=
"w-full"
>

 Login with Google

</
Button
>


</
CardFooter
>


</
Card
>


)

}

Enter fullscreen mode

Exit fullscreen mode

This is just a sign-up page.

You know what?

I checked Chakra UI and loved their card implementation even more.

Watch this…

import

{

Avatar
,

Button
,

Card

}

from

"
@chakra-ui/react
"

const

Demo

=

()

=>

{


return
(


<
Card
.
Root

width
=
"320px"
>


<
Card
.
Body

gap
=
"2"
>


<
Avatar
.
Root

size
=
"lg"

shape
=
"rounded"
>


<
Avatar
.
Image

src
=
"https://picsum.photos/200/300"

/>


<
Avatar
.
Fallback

name
=
"Nue Camp"

/>


</
Avatar
.
Root
>


<
Card
.
Title

mt
=
"2"
>
Nue Camp
</
Card
.
Title
>


<
Card
.
Description
>

 This is the card body. Lorem ipsum dolor sit amet, consectetur
 adipiscing elit. Curabitur nec odio vel dui euismod fermentum.
 Curabitur nec odio vel dui euismod fermentum.

</
Card
.
Description
>


</
Card
.
Body
>


<
Card
.
Footer

justifyContent
=
"flex-end"
>


<
Button

variant
=
"outline"
>
View
</
Button
>


<
Button
>
Join
</
Button
>


</
Card
.
Footer
>


</
Card
.
Root
>


)

}

Enter fullscreen mode

Exit fullscreen mode

What did you notice common in these demos?

They have a parent component and child components that somehow come together to make things work.

….and voila…you have a card component.

Chakra UI even goes a step further to do something weird.

<
Card
.
Root
>


<
Card
.
Description
>


</
Card
.
Description
>

</
Card
.
Root
>

Enter fullscreen mode

Exit fullscreen mode

Can JSX now do dot notations?!!

How do all these work?

This whole thing is known as composition.

In React terms, it's called compound components.

This is how you build UIs for scalability, reusability, and separation of concerns.

And that's why these big UI libraries employ that.

Now, why do you use them? How do you use them? When should you use them? I'm answering all these questions in a moment.

## The big question: why?

I applied to a frontend role earlier this week and was taken to the next stage of assessment.

We were told to build a checkout page and were presented with the UI on Figma.

Long story short, this is what it looks like…

Very simple.

It's also live. You can check it out:https://crypto-checkout-omega.vercel.app/

Now, how do you build a checkout like this, thinking in systems?

Focus on this word…

Utility.

## Inversion of Control

I'll digress a bit to talk about building a simple onboarding page.

Very simple.

if
(
step

===

1
)

{

...

}

else

if
(
step

===

2

&&

isBusiness
)

{

...

}

else

if
(
step

===

2

&&

!
isBusiness
)

{

...

}

else

if
(
step

===

3

&&

country

===

'
NG
'
)

{

...

}

Enter fullscreen mode

Exit fullscreen mode

Right?

To be fair, this is a good implementation.

...but very far from an enterprise-grade solution.

It struggles with maintainability, scalability, and reusability.

It actually looks a lot better in my illustration.

I've seen situations where this gets to 700 lines of code with so many conditions, and it becomes difficult to wrap your head around it.

Do you want to know what a Composition (Compound Components) implementation for this looks like?

<
Onboarding
>


<
Onboarding
.
Step

id
=
"account"
>


<
AccountSetup

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Step

id
=
"kyc"
>


<
KYCForm

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Step


id
=
"business"


when
=
{
userType

===

'
business
'
}


>


<
BusinessDetails

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Step


id
=
"bank"


when
=
{
country

===

'
NG
'
}


>


<
BankAccount

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Complete

/>

</
Onboarding
>

Enter fullscreen mode

Exit fullscreen mode

And that's basically every code.

Composition is a design pattern in which multiple components are designed to work together by sharing implicit state and behavior.

It works with something called "Inversion of control."

Inversion of Controlis a design principle where the flow of control is delegated to a higher-level component, rather than being explicitly managed by the consumer.

In simpler terms:

* Traditional control: You call the code
* Inverted control: The code calls you

Here's what I mean…

#### Traditional Control…

<
Checkout


amount
=
{
5000
}


paymentMethod
=
"card"


onPaymentMethodChange
=
{
setMethod
}

/>

Enter fullscreen mode

Exit fullscreen mode

#### Inverted Control…

<
Checkout
>


<
Checkout
.
Amount

/>


<
Checkout
.
PaymentMethods

/>


<
Checkout
.
Submit

/>

</
Checkout
>

Enter fullscreen mode

Exit fullscreen mode

The component "Checkout" basically handles state and logic, while you control the layout by how many "child components" you choose to put out.

If, for instance, I now want to have a forward feature, I only throw in a<Checkout.Forward />component to handle that.

<
Checkout
>


<
Checkout
.
Amount

/>


<
Checkout
.
PaymentMethods

/>


<
Checkout
.
Submit

/>


<
Checkout
.
Forward

/>

</
Checkout
>

Enter fullscreen mode

Exit fullscreen mode

Say you're building a checkout page that has limited features for certain countries due to restrictions. This becomes a beauty to handle.

## Utility driven

Composition becomes very useful when you're building single components that aim to be "utilitarian".

E.g., Imagine building a Card UI like Chakra UI does.

So you write

export

function

Card
({


title
,


subtitle
,


description
,


imageUrl
,


imageAlt
,


showHeader

=

true
,


showFooter

=

true
,


primaryActionLabel
,


onPrimaryActionClick
,


secondaryActionLabel
,


onSecondaryActionClick
,


footerText
,


isLoading
,


disabled
,


theme

=

'
light
'
,

}:

CardProps
)

{


return

(


<
div

className
=
{
`card card--
${
theme
}
`
}
>

Enter fullscreen mode

Exit fullscreen mode

Hectic!

You'll have so many moving parts (that would never be enough) sent as props. So many things to remember. And yet not with much control.

At this point, Composition saves the day.

<
Card

theme
=
"dark"
>


<
Card
.
Header
>


<
h3
>
Premium Plan
</
h3
>


<
p
>
Best for teams
</
p
>


</
Card
.
Header
>


<
Card
.
Image

src
=
"/plan.png"

alt
=
"Plan image"

/>


<
Card
.
Body
>


<
p
>
Unlimited projects and advanced analytics
</
p
>


</
Card
.
Body
>


<
Card
.
Actions
>


<
button
>
Subscribe
</
button
>


<
button
>
Learn more
</
button
>


<
small
>
Cancel anytime
</
small
>


</
Card
.
Actions
>

</
Card
>

Enter fullscreen mode

Exit fullscreen mode

Voila, that's all you need!

## Implementing Compound Components

Now, let's go back to our onboarding illustration.

<
Onboarding
>


<
Onboarding
.
Step

id
=
"account"
>


<
AccountSetup

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Step

id
=
"kyc"
>


<
KYCForm

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Step


id
=
"business"


when
=
{
userType

===

'
business
'
}


>


<
BusinessDetails

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Step


id
=
"bank"


when
=
{
country

===

'
NG
'
}


>


<
BankAccount

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Complete

/>

</
Onboarding
>

Enter fullscreen mode

Exit fullscreen mode

Here's how we can implement this…

#### Onboarding.tsx

const

OnboardingContext

=

React
.
createContext
<
any
>
(
null
);

export

const

Onboarding

=

({

children

}:

{

children
:

React
.
ReactNode

})

=>

{


const

[
currentStep
,

setCurrentStep
]

=

React
.
useState
(
0
);

// Filter steps based on "when" prop


const

steps

=

React
.
Children
.
toArray
(
children
).
filter
(


(
child
:

any
)

=>

child
.
props
.
when

!==

false


);


const

value

=

{


currentStep
,


totalSteps
:

steps
.
length
,


next
:

()

=>

setCurrentStep
((
s
)

=>

s

+

1
),


prev
:

()

=>

setCurrentStep
((
s
)

=>

s

-

1
),


};


return
(


<
OnboardingContext
.
Provider

value
=
{
value
}
>


{
steps
[
currentStep
]}


<
/OnboardingContext.Provider
>


);

};

Enter fullscreen mode

Exit fullscreen mode

We build a filter method that filters children with a truthy "when" prop value.

We track currentStep ID and setCurrentStep, and made sure to put it in React Context.

This allows the relevant components down the line to change the "currentStep" for themselves globally.

#### Step Component

Onboarding
.
Step

=

({

children

}:

{

children
:

React
.
ReactNode

})

=>

{


return

<>
{
children
}
<
/>
;

};

Enter fullscreen mode

Exit fullscreen mode

#### Complete Component

Onboarding
.
Complete

=

()

=>

{


return

<
div
>
🎉

Onboarding

complete
!<
/div>
;

};

Enter fullscreen mode

Exit fullscreen mode

The most important part of this implementation is the display logic.

 {steps[currentStep]}

Enter fullscreen mode

Exit fullscreen mode

"steps" is an array of React children.

The index "[currentstep]" lets React know what children to display at any point.

E.g steps[0], steps[1].

Remember, every component inside the Onboarding Context Provider has access to currentSteps and setCurrentSteps, so can easily move the step of the whole onboarding.

#### Final usage…

<
Onboarding
>


<
Onboarding
.
Step

id
=
"account"
>


<
AccountSetup

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Step

id
=
"kyc"
>


<
KYCForm

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Step


id
=
"business"


when
=
{
userType

===

'
business
'
}


>


<
BusinessDetails

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Step


id
=
"bank"


when
=
{
country

===

'
NG
'
}


>


<
BankAccount

/>


</
Onboarding
.
Step
>


<
Onboarding
.
Complete

/>

</
Onboarding
>

Enter fullscreen mode

Exit fullscreen mode

PS: If you're smart, you may notice...

<Onboarding.Complete />

Enter fullscreen mode

Exit fullscreen mode

...was left out.

With our current logic, it'll be left out since the "steps" array filters out React children without a truthy "when" prop value.

How do we fix this?

Let's adjust the logic a lil bit...

 const steps = React.Children.toArray(children).filter((child) => {
 if (React.isValidElement(child)) {
 // Only include Step components with when !== false
 if (child.type === Onboarding.Step) {
 return child.props.when !== false;
 }
 }
 return false;
 });

Enter fullscreen mode

Exit fullscreen mode

This works because every React child has a type object, which is actually the name of the component.

Hence, we can use that to explicitly sort out only the steps component, Onboarding.Step.

## Back to my Interview

This is what my final parent "Checkout" component looked like

<
Checkout
>


<
Checkout
.
TransferTabs

/>


<
Checkout
.
Body
>


<
Checkout
.
CryptoToCash

when
=
"crypto-to-cash"

/>


<
Checkout
.
CashToCrypto

when
=
"cash-to-crypto"

/>


<
Checkout
.
CryptoToFiat

when
=
"crypto-to-fiat-loan"

/>


</
Checkout
.
Body
>


</
Checkout
>

Enter fullscreen mode

Exit fullscreen mode

So how did I implement this?

Think deeply (maybe ask ChatGPT 😂).

Actually, the github repo is available @https://github.com/ebubesunday16/crypto-checkout.

Side quest: I'm still jobhunting! Would take any job at this point. Portfolio is athttps://me.soapnotes.doctor

## Don't Overengineer

If it's a utilitarian component. Engineer. Not a utilitarian component? Do not engineer.

E.g., I still comfortably had this somewhere in my code…

<
AmountInput


label
=
'You pay'


value
=
{
payingAmount
}


onChange
=
{
handlePayingAmountChange
}


placeholder
=
"0.00"


selectedCrypto
=
{
selectedPayingCrypto
}


onCryptoChange
=
{
setSelectedPayingCrypto
}

/>

Enter fullscreen mode

Exit fullscreen mode

Unless I'm also going to build a calculator and so badly want to cling to the logic I had with it (which is beautiful, btw), there's no need to make "AmountInput" a compound component.

It has only one purpose to serve me, and not many moving parts.

Love and light. Peace ✌️

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

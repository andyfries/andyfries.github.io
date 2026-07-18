---
layout: post
title: Inputs Not Outputs
---

I’m about as far from an AI luddite as you can get. I was an early adopter of many AI coding tools, I host meetups to discuss the latest developments, I rarely even open an IDE nowadays.

But I never let AI write for me.
<!--more-->

## AI Produces Bad Writing Outputs
This didn’t start as a dogmatic position. As I adopted AI into more of my professional life I tried using it for research, editing, and wholesale document creation. Through that experimentation I repeatedly found it not just worthless but detrimental for large parts of the writing process.

You’ll recognize this feeling if you’ve ever been asked to review a 10 page screed filled with `code blocks`, **emphasis**, and clickbait headings like *The Subtle Takeaway*. Much has been said about the “AI voice” and how to avoid it, but this isn’t a syntax problem. It extends to the root of the endeavor: AI writing is bad at building shared understanding.

When you write a design doc recommending the creation of a new component to serve some use case, what does that document need to communicate to readers? They need to understand the problem, the context it exists within, the tradeoffs available, and how the proposed solution implements those tradeoffs. As the author you need to balance the detail required to frame the problem against the [cognitive burden](https://andyfries.com/quality-code-review-feedback/) imposed on your audience. This takes a lot of practice, editing, and empathy.

When you prompt an AI model to write that document, it does so with all the gusto of a toddler describing their favorite dinosaurs. You’ll get 3 paragraphs on why one database is unsuitable for the problem before the document even mentions the access patterns. Discussions of the API design lead with a half-page blob of GraphQL schema without giving the reader any foundation to understand why those shapes are important or how they affect critical behaviors like pagination. It’s bad enough when the information is accurate, but hallucinations can transform worthless writing into an [info hazard](https://en.wikipedia.org/wiki/Information_hazard) by undermining the reader’s domain knowledge.

Considerations of empathy and cognitive burden have no place in these glorified Markov chains. The fact that there is any information at all to be gleaned from these inaccessible piles of technical prose is miraculous.

Documents are a [tool to solve problems](https://andyfries.com/why-write/), and using AI to write dulls that tool. I’m tempted to ascribe this fact to a philosophical principle, such as the fundamental folly in trying to connect humans and machines, but whatever the cause the result fails the reader and the “author”.

## AI Produces Excellent Writing Inputs
With all that said, walling off AI from the writing process entirely would be a mistake. The key is how you use it.

AI models are faster at research than I will ever be. They can source examples, cite references, and find prior art in seconds when the same task would take me days. These sources allow me to confidently recommend a particular approach knowing how it fits into the technical landscape. Crucially, grounding the research in references and manually synthesizing those into my own conclusions is a guard against the insidious hallucinations that often undermine AI writing.

To a lesser extent, they’re also useful for feedback. I’ve had moderate success with prompting AI models to analyze the logical flow of an argument or flag inconsistencies in tense. The feedback is worthless as often as not, but it’s an improvement over what I’m able to catch independently. For example, I went back and forth with an AI model when editing [Why Write? (Original Draft)](/why-write-original/) before arriving at the [published version](/why-write). I retained my voice by seeking the spirit of the feedback rather than blindly applying recommendations.

## Inputs, not Outputs
So much of the value of writing is in the process. Augmenting the inputs to that process strengthens it; outsourcing the outputs circumvents it.

This doesn’t just fail readers, it also deprives authors. One of the main problems documents solve is sorting out your own thinking: why does this project matter? do I understand the tradeoffs in choosing one approach over another? how will this choice limit our options in the future?

AI writing might get better over time, and it may even grow to rival humans in communicating ideas, but it will never improve _your_ thinking.

--------

### Postscript - What About Code?
There’s an unresolved tension in this essay. I use AI to generate code (i.e. create an output) all the time. Why is that any different than a document?

The difference is a matter of degree rather than kind. I do practice this principle with code, and [not just my code](/reviewing-code/) either, but the focal point in that process is more on editing than creation. I hardly hand-write code anymore, but when I do it’s _re_-writing to reduce cognitive burden. This wasn’t the case even a year ago, but models are now creating quality code frequently enough that I’m comfortable abdicating control over that layer.

I think the reason for this is the domain. Functional code is verifiable and machines are a primary consumer (some would argue machines are quickly becoming the _only_ consumer), while effective prose is judged subjectively with humans as the primary consumer. The reinforcement learning at the heart of modern LLMs has arguably surpassed human ability in coding, but I’m not convinced this technology is capable of doing the same for communication.
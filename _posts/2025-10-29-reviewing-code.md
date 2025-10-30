---
layout: post
title: Reviewing Code
---

I'm bad at reading code. That's made me a better code reviewer.

<!--more-->

Early in my career I was advised to develop my coding skills by reading the source code for a popular project like the Linux kernel or Redis and I was ashamed to get nothing from it. I'd spend a while trying to perceive the technical lessons that supposedly awaited me in those codebases only to end up frustrated and none the wiser.

Even now -- more than a decade into my career of working with code -- reading it feels difficult. I’m slow to understand structure and it can take me many passes to grok the full approach. Surprisingly, this hasn’t hindered my growth as a code reviewer. At first I tried to mask this as a technical shortcoming, thinking I was succeeding as a reviewer despite my code reading difficulty, but now I realize it’s the opposite. I’m a _better_ reviewer because I have a hard time reading code.

This problem is a superpower in disguise. By struggling to read code, I’ve become more sensitive to things that improve or hinder readability. The value of this might seem dubious until you consider how many “best practices” can be reframed as readability problems. The [single responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle) is an oft-cited guideline for better cohesion in classes, but it also speaks to a readability issue: is it easier to read an implementation doing one thing or a variety of things? The [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle) can be reframed as the [principle of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment): it’s less confusing when subclasses are consistent with parent behavior.

My review process is a collection of these heuristics:
- If I have to reread a function repeatedly before I understand it, that's a sign something about it is subtle, unintuitive, or overly complex. 
- If I get confused about where I'm at in a class with multiple similar methods, that's a sign their use isn't distinct enough. 
- If I'm surprised by the usage of a variable, that's a sign its scope or name isn't obvious. 
- If I see the same pattern in multiple classes without a unifying structure that makes it apparent, that's a sign an abstraction like inheritance or composition might be needed to communicate the pattern to readers.

Abstracting this into a general approach to reviewing code is delightfully simple. No need to memorize design patterns or the five SOLID principles, just read the code and pay attention to anything that feels surprising or confusing. For each potential issue, reflect on why it feels off then recommend a change that would make it easier to read.

Identifying the right fix can be difficult without enough technical depth, but the rest of the process is remarkably accessible; it doesn’t take much experience to be able to point out the confusing parts of an implementation.

Besides being accessible, the main reason to review for readability is that it’s incredibly effective. I often hear that my code reviews are unusually substantive and useful, especially in architectural areas, but even my most technical feedback starts with my experience as a reader of the code. 

I stumbled onto this approach out of necessity but I’d recommend it to anyone. Next time you’re reviewing a change, ask yourself: is it easy to read? You might be surprised at how useful the answer is.
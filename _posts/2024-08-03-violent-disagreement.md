---
layout: post
title: Violent Disagreement
---

Years ago, a mentor of mine introduced me to the concept of "violent disagreement". Initially I balked at the idea of _violently_ opposing anything in a professional setting, but in time it has become one of my most used tools in making quality decisions quickly and at scale. In this post I'll dive into what it is, how to do it, why it works, and when to use it.

## What

First, let's cover the obvious. We're using "violent" in the sense of strength and intensity, not physical force. While "violent disagreement" may sound extreme and a bit jarring, it's a common phenomenon you likely recognize, if not by name. When someone proposes shipping a change to prod without going through the usual testing procedures and you try to remain composed while telling them in no uncertain terms how terribly that could go wrong, that's violent disagreement. When a partner team proposes a design that would increase load on your team's services by 100x and you want to discuss tradeoffs and alternatives before implementing it, that's violent disagreement. 

In short, violent disagreement is a concern that must be addressed before proceeding.

## How

Remember, the violence here comes from the intensity of conviction, not from its expression. When raising a concern of this level of importance, remain mindful of the goal: you are working together to solve a problem. You're helping a peer recognize an issue that might impede that goal. Notably, your tone should not emphasize their oversight or exaggerate the severity of the problem. Focus on the facts and finding a path forward together.

Conversely, if someone is raising disagreement with your proposal, discuss whether it's severe enough to be blocking (i.e. violent disagreement) or something that can be addressed separately/in parallel. Again, the focus is on making progress together, not sweeping their feedback aside as non-blocking. Even if their concern isn't blocking, ensure it's sufficiently addressed to retain their trust in delivering the larger initiative.

## Why

Raising violent disagreement marks a clear decision point for everyone involved. This is the first major benefit. If you've ever been a part of a code review comment thread that won't seem to end, or a standoff between engineers and PMs on whether a feature can/should be included for a milestone, you're familiar with what happens when decision points aren't clear. Issues are raised, arguments are made, individuals dig in, and progress grinds to a halt. Framing issues as violent disagreement can break this deadlock: is the concern severe enough to require a change of plan, or can it be mitigated otherwise?



## When

Violently disagreeing should be a high bar. It's a threshold that should only be breached when there is a significant chance of negative impact if a proposal proceeds. Aggressively categorize concerns, including your own, by whether they constitute violent disagreement. If you're raising an issue that does not constitute violent disagreement, make that clear and separate the concern from the deliverable at hand. 

Violent disagreement is a tool for resolving ambiguity in conflict. I've frequently applied it in code reviews where I publish a commit and a reviewer requests tons of time-consuming changes. I then discuss with them which of those changes feel like blocking issues and prioritize accordingly. There is an element of social graces here; pick your battles and give your reviewer the benefit of the doubt on matters you can resolve quickly with little effort.

Another common application is in design reviews. When someone raises a concern about your proposed design, seek to understand the intensity of that concern. Is it a shallow curiosity, are they lacking some context about the specific situation, or are they speaking from experience about a severe issue you're likely to encounter? 

When you ask someone for feedback, whether it be on a code review, system design, or otherwise, they'll tend to give you some. Use the concept of violent disagreement to discern what they want you to do with it.

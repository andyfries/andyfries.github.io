---
layout: post
title: 'How to Get Higher Quality Code Review Feedback: Reduce Cognitive Burden'
---
Reduce the cognitive burden on reviewers when publishing a code review. Using this as your guiding principle, you'll write higher quality code, ship it faster, and earn more trust with your colleagues. Let's dive into how that looks practically.

<!--more-->

## Reviewing Takes Resources

First, we need to understand the problem. Why might reviewers give low-quality feedback? In my experience, it tends to come down to limited resources. Time, attention span, mental load - it takes a lot to review code. If you're a reviewer running low on any of these, you may leave feedback less about the substance of the change and more about surface-level nitpicks or logistical questions (e.g. how will this be deployed). I've noticed that I tend to leave non-committal feedback when put in this position, responding to the review to get it off my todo list but not feeling comfortable enough to approve it or send it back for rework.

## Minimize Cost of Reviewing

As someone looking to get a change reviewed and merged, it can be infuriating to get a bunch of review feedback without a clear sense of whether the reviewer is aligned with the substance of the change. We're out hours/days of waiting time, we need at least one more cycle of back and forth with the reviewer, and we have a list of feedback that may feel peripheral to the current work. This is the failure mode we're trying to avoid. 

How do we make it easier for reviewers to give quality feedback? We eliminate everything else from the review except the most important pieces, then give them all the context they need to understand it. Below are some tips on how to do so. But first, how do we know what it's like to review our code? 

## Be Your Own Reviewer

Before asking others to give their time to review your changes, go through them yourself first. This is one of the most effective practices I've found for making the whole review process go smoothly. Not only does it respect your reviewer's time by catching the easy stuff, but it also gives you a chance to save face by fixing mistakes before others see them. 

I often go through two or three revisions of a code review before it's even published. The gap between "functional" and "easy to review" can be vast. Adopting this practice gives you a quick feedback loop to know if the review is framed effectively. Now let's put it into practice with a few pragmatic tips.

## Reducing Cognitive Burden

### Limit Changes

If your code review has a big diff of formatting changes mixed in with meaningful business logic, guess which one a reviewer is likely to comment on when they're low on time? Limiting changes in the review to a single purpose avoids this problem by keeping the reviewer's attention on what matters.

My rule of thumb is to avoid working for more than a week without publishing something for review. It's easy to pile up a stack of changes all building towards a big feature, but publishing a multi-page review after weeks of work is a recipe for frustration on all sides.

### Provide Context

As you go through your changes, ask yourself whether any critical pieces aren't immediately obvious. Are there any functions that behave surprisingly? Is there a new enum that seems inconsequential but turns out to be crucial? Are there security implications for the order of API calls? 

Any time you notice something like this, try to eliminate the opportunity for confusion. Refactor the surprising function, move the enum closer to its usage, make it impossible to use the APIs in the wrong order. If you can't eliminate the issue, add context. Put a comment in the code or link a design document, just be sure to put it in writing where your reviewer can't miss it. A subtle benefit here is that writing out the justification forces you to think through it; I've often gotten halfway through justifying something and realized I could eliminate it with some refactoring.

An extreme version of this tip is to write a detailed design in the review description. I've used this approach for particularly complex or sequenced changes to ensure everyone understands what the change entails and how it relates to the larger picture. You can see excellent examples of this on the LKML (Linux kernel mailing list), such as [this change](https://lkml.org/lkml/2020/12/13/284).

### Get Buy-In

As a reviewer, it's always unpleasant to realize that I disagree with the author on some foundational issue. Instead of polishing up a finished implementation, now the author and I have to backtrack to hashing out the basic approach. Worse, there's often a strong bias towards doing it one particular way because that code has already been written. Best case scenario we both lose some time to getting ourselves aligned. Worst case scenario the author has to redo the bulk of the change because of some critical flaw.

You can avoid this by getting buy-in upfront. Talk to your stakeholders, make sure they're on board with the proposed solution, and iron out any disagreements before implementing anything. This isn't necessary for more trivial changes, but it's vital for anything with broad implications. 

With major decisions discussed in advance, reviewers will be free to focus on the _how_ of the change rather than the _why_.
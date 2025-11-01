---
layout: post
title: Reviewing Code
---

This is a companion piece to [link to quality code review feedback], intended for code reviewers rather than code authors.

Many engineers review code begrudgingly. In their minds it's an obstacle to the real work or an exercise in rubber stamping. They offer critique only when it rises to the level of [violent disagreement](LINK TBD), perhaps justifying their lack of feedback as a kindness: the author already put in the time to make this change, I don't want to inconvenience them unless it's critical.

But what if it wasn't an inconvenience? What if the author is making a [bid for connection](https://www.peps.org/files/bids-for-connection), requesting an opportunity to improve their craft, and you're turning away from it by wordlessly stamping? 


In my experience the truth is often somewhere in between. Some authors really do seek constructive criticism, some are expecting a rubber stamp, and code reviews -- like all interpersonal communication -- are therefore highly contextual. But I often make a conscious choice to offer my code review feedback in the spirit of learning even if the author isn't in a position to engage with that at the time. As a historical artifact of the codebase, my code review feedback isn't merely for the author but also any future readers.

-----

I spend a lot of my time reviewing code. Besides the obvious fact that it's a major output of the engineering organizations I'm part of, I also just really enjoy it. There are few aspects of software engineering that provide such an immediate set of opportunities for learning and mentoring as code reviews. 

I've long delayed this essay because I've struggled to identify what I could add to the topic. 

There are many great posts on the mechanics of reviewing code: what to look for at a technical level (post by Kevin London)[https://www.kevinlondon.com/2015/05/05/code-review-best-practices/], creating a healthy organizational culture (Google engineering practices)[https://google.github.io/eng-practices/review/reviewer], navigating the interpersonal dynamics (post by Michael Lynch)[https://mtlynch.io/human-code-reviews-1]. 

-----

I'm not the kind of engineer that has an encyclopedic knowledge of design patterns. I don't own a copy of Clean Code and I rarely reference computer science principles in my code reviews. Part of that is practical: as a product engineer these things don't come up as often as they might in other disciplines. But it's also a reflection of my broader approach to software: code is meant to be read, therefore my reviews focus almost solely on the reading experience.

As a guiding principle this has taken me surprisingly far. I often hear that my code reviews are unusually substantive and useful, especially in architectural areas, but even my most technical feedback starts with my experience as a reader of the code. My process is one of heuristics based on my ability to read and understand the code. Earlier in my career I mistrusted these heuristics, telling myself that an inability to understand the code was a shortcoming of my technical ability rather than a property of the code itself, but over time I've come to embrace the phenomenon. Some amount of that is a rejection of impostor syndrome, but the more compelling motivation is an altruistic one: if I don't understand the code then it's likely someone else won't either. If I can embrace that inability to understand publicly, a prospect that's certainly made more comfortable by my identity as a white male native English speaker, then maybe I can raise concerns shared by others less comfortable voicing their opinions publicly.

If I have to reread a function repeatedly before I understand it, that's a sign something about it is subtle, unintuitive, or it may overly complex. If I get confused about where I'm at in a class with multiple similar methods, that's a sign their use isn't distinct enough. If I'm surprised by the usage of a variable, that's a sign its scope or name isn't obvious. If I see the same pattern in multiple implementations without a unifying structure that makes it apparent, that's a sign an abstraction like inheritance or composition might be needed to communicate the pattern to readers.

The result of these heuristics is nothing special; they're the same comments you might make if you analyzed the implementation through the lens of things like the Liskov substitution principle or Kolmogorov complexity. The difference is at a human level: I can't identify these things if I analyze code from more academic lenses. It took me a while to admit that, and part of me still sees it as a shortcoming, but over time I'm becoming increasingly convinced it is an equal and valid approach to reviewing code. 

An unexpected benefit of this approach is that the impact of my suggestions are grounded in the reading experience. If I recommend the author introduce an interface for shared logic between components, I have confidence that's a meaningful change because it would make that aspect of the implementation more apparent to me as a reader. Whether it's a worthwhile change is of course a matter of opinion, and the author may disagree with me on that.

------

## Background
I'm bad at reading code. Early in my career I was advised to develop my coding skills by reading the source code for a popular project like the Linux kernel or Redis and I was ashamed to get nothing from it. I'd spend a while trying to perceive the technical lessons that supposedly awaited me in those codebases and end up tired, frustrated, and none the wiser. If this was the road to getting better then I was in for a rough ride.

Thankfully, I stumbled across another way to improve: code reviews. Many of my coworkers would rubber stamp my review requests, but a handful of the more senior (read: opinionated) engineers would ruthlessly mark up my changes. From those reviews I learned what signs they looked for to know when an implementation needed to change, the patterns they applied to make code more ergonomic, and what kinds of changes made them nervous. In time I internalized these lessons and developed my own sense of what made good code. Although it was uncomfortable to receive a review from an engineer ten years my senior pointing out a dozen issues in my code, it was invaluable in helping me grow to the engineer I am today.

## Readability
Now as a staff engineer more than a decade into my career, I find myself increasingly on the reviewing end of code reviews. I take a lot of pride in my ability to give quality code review feedback (see my previous post on [how to receive quality feedback](LINK)) but I've struggled to articulate my process. After reflecting on it, I realized my entire approach to reviewing code can be summed up in a single question: is it easy to read?

I’ll admit part of me is skeptical of professing this guiding principle of readability in reviewing code. After all, it wasn’t that long ago that I was bad at reading code. To be honest I’m not sure I’m much better at it now even after years of practice. Who am I to talk about readability?

But this problem is a superpower in disguise. By struggling to grok written code, I’ve become more sensitive to things that improve or hinder readability. This might seem more like a recipe for pedantry than quality code review feedback[^1] until you consider how many “best practices” can be reframed as readability problems. The [single responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle) is an oft-cited guideline for better cohesion in classes, but it also speaks to a readability issue: is it easier to read an implementation doing one thing or a variety of things?

My review process is a collection of these heuristics. If I have to reread a function repeatedly before I understand it, that's a sign something about it is subtle, unintuitive, or it may overly complex. If I get confused about where I'm at in a class with multiple similar methods, that's a sign their use isn't distinct enough. If I'm surprised by the usage of a variable, that's a sign its scope or name isn't obvious. If I see the same pattern in multiple classes without a unifying structure that makes it apparent, that's a sign an abstraction like inheritance or composition might be needed to communicate the pattern to readers.

The result of these heuristics is nothing special; they're the same comments you might make if you analyzed the implementation through the lens of things like the Liskov substitution principle or Kolmogorov complexity. The difference is at a human level: I can't identify these things if I analyze code from more academic lenses. It took me a while to admit that, and part of me still sees it as a shortcoming, but I’m beginning to embrace the fact that this simple technique is the secret to my success as a code reviewer.

## Counterargument
Readability is a subjective measurement. For some this is enough to discredit the idea entirely. To those readers I would offer a reminder that as long as humans are involved, subjectivity is unavoidable.

There is a more nuanced version of this argument though. Because readability is subjective, using it as a guiding principle is optimizing for the comfort of the most outspoken reviewer. In a dysfunctional team this might result in endless bikeshedding or a dictatorial dynamic.

This is a fair point. I’ve been on the receiving end of nonsense suggestions made in the name of readability (and, if I’m being honest, given some myself). It gets worse when the problem space is inherently complex like distributed systems; the threshold for “readable” is pretty different once concurrency mechanisms get involved.

To me this is more a reason for discretion than a refutation of the technique itself. I’m judicious in making comments that have minimal impact, focusing instead on the areas of greatest friction. 

[^1]: We’ve all gotten those less than helpful comments like “you should adopt Hungarian notation to make this more readable” or “this would be more readable in Java instead of Python”. 

-----

## Code Reviews as Mentorship
Early in my career I was advised to develop my coding skills by reading the source code for a popular project like the Linux kernel or Redis and I was ashamed to get nothing from it. I'd spend a while trying to perceive the technical lessons that supposedly awaited me in those codebases only to end up frustrated and none the wiser. If this was the road to getting better then I was in for a rough ride.

Thankfully, I stumbled across another way to improve: code reviews. Many of my coworkers would rubber stamp my review requests, but a handful of the more senior (read: opinionated) engineers would ruthlessly mark up my changes. From those reviews I learned what signs they looked for to know when an implementation needed to change, the patterns they applied to make code more ergonomic, and what kinds of changes made them nervous. In time I internalized these lessons and developed my own sense of what made good code. Although it was uncomfortable to receive a review from an engineer ten years my senior pointing out a dozen issues in my code, it was invaluable in helping me grow to the engineer I am today.

Code reviews are one of the most important mentorship opportunities we have as software engineers. They are explicit requests for technical feedback. But what does it look like to thoroughly review code? How does one learn to do that?

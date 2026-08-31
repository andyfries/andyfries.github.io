---
layout: post
title: Abolishing Human Code Review
---

Many in AI circles have declared that the human code review is dead. My knee-jerk reaction has been to dismiss this as AI hype. After thinking through it, not only do I think it’s a good idea, it might even be doable.
<!--more-->

## The Plan
To keep this exercise feasible I’ll make two stipulations. First, there are interpersonal trust dynamics in any system owned by more than one person. While the trust issue is important, I’m more curious about the rest of the problem space, so I’m going to simplify the discussion by asking what it would take for me to confidently ship one of my own changes to production without another human reviewing it. Meeting that standard is the lower bound on what I’d need to confidently ship changes I didn’t author.

Second, there is value in advancing towards abolishing human code review even if that goal isn’t reached. Anything that makes changes easier to review, more likely to be correct, or less dangerous is valuable in its own right.

With this in mind we can view the question as a [forcing function]({% post_url 2026-05-17-embracing-difficulty %}): if you didn’t have human code reviews, how would you continue to uphold engineering standards?

## The Purpose of Code Review
Let’s start with [Chesterton’s fence](https://fs.blog/chestertons-fence/) and consider the purposes code reviews serve.

The obvious purpose of code review is to ensure changes are correct before merging. But calling code review a correctness gate is too narrow a definition.

Code reviews also increase diversity of thought. I’ve had many correct PRs nevertheless undergo significant refactors because a teammate suggested a better approach. Conversely, I’ve helped many teammates improve their changes by raising cross-cutting concerns from another project or lessons learned from past experience.

Finally, code reviews serve as teaching opportunities for authors and reviewers. Newer engineers, those less familiar with the domain, or even experienced engineers out of the loop on that particular project can all benefit from an explicit opportunity to discuss the purpose and merits of a change.

For each of these three purposes, we can now consider what it would take to accomplish them without human code reviews:
1. Enforce the quality of a change
2. Diversify thought
3. Educate

### Enforce Quality
Engineers have been architecting systems to enforce quality for decades; this isn’t a new problem in the age of LLMs, but it’s certainly amplified.

We already have industry best practices here: more tests, better documentation, automated rollbacks, etc. The techniques we need to protect codebase quality are the same techniques we’ve always needed, [only more so]({% post_url 2026-03-15-reviewing-llm-code %}).

That’s fine in the abstract, but what would it take to do this in reality? To answer this question, I’ll use the scenario of shipping my own change to production as a starting point. In this scenario I have reasonable confidence in the correctness of my change and I’m aware of the technical and business environments in which it’s being made.

My team owns the homepage of Airbnb, a crucial entry-point that sits atop a tall stack of dependencies, so our bug surface area is large and our risk tolerance is low.

For me to have confidence shipping my change to production without another human reviewing it, I would require:
* an automated review checking:
	* the quality of my change against codebase standards
	* potential conflicts with other in-flight work on the surface (e.g. A/B tests, API redesigns)
* reliable documentation for any APIs involved in the change
* a feature flag gating the functionality
* automated tests covering:
	* end-to-end behavior of the change and any existing functionality on that surface it may impact
	* latency profiling to highlight any impact to the critical path
	* load testing with any affected dependencies to ensure they can scale with new traffic patterns
* a continuous delivery pipeline to deploy the change with as few other changes as possible to minimize confounding variables
* automated rollback monitors on either the feature flag or the deployment, instrumented thoroughly with KPIs on user behavior and system health

Many of these obstacles are hard but eminently solvable with current technology. We can therefore consider the quality responsibility addressed and shift to the more human aspects of code review.

### Diversify Thought
Taking my own advice to [build more tools]({% post_url 2026-05-30-building-more-tools %}), I recently shipped an internal tool spanning multiple APIs, complex data modeling, and new dependencies. There were decision points throughout that process where I sought feedback from domain experts to confirm my approach solved the right problems in the right ways.

Despite that complexity, code reviews for my implementation were brief and uneventful. I attribute this to [writing]({% post_url 2026-06-12-why-write %}) extensively about the problem to disconfirm my biases and drive alignment with stakeholders. By the time I got to the code, there wasn’t much discussion left to have.

Getting buy-in before code is written was already a practice I [advocated for]({% post_url 2024-08-04-quality-code-review-feedback %}#get-buy-in), but it may also provide the same diversity of thought generated from human code review.

Continuing our standard of confidently shipping my own change to production without human review, I would require:
* a change sufficiently low risk or low complexity that diversity of thought isn’t a concern, OR
* a [human-authored document]({% post_url 2026-07-18-inputs-not-outputs %}) describing the purpose of the change and any major implementation decisions being made
* approval on that document from engineers with broad domain context

These requirements suggest a high quality technical document may be a substitute for the role of code reviews in diversifying thought. I’m not the first to come to this conclusion: Sean Grove of OpenAI gave a [talk](https://www.youtube.com/watch?v=8rABwKRsec4) on this theme in 2025, and Ankit Jain of Aviator (code review tooling) espoused spec-driven development in a [post](https://www.latent.space/i/189703430/from-reviewing-code-to-reviewing-intent) earlier this year.

### Educate
The shift towards agentic engineering has not been kind to many junior engineers, and I am loath to deprive them of another opportunity to learn in the form of code reviews. Even for experienced engineers, the increased pace of change means it’s harder to keep track of important projects.

What would it take to supplant this role that human code reviews serve? While my requirements for the other roles felt obvious, this area feels more nebulous. What does it even look like for education opportunities to be well served in an engineering team?

I’d begin with a simple survey. Ask your engineers whether they have visibility of the work happening in their space and whether they’re able to grow their skills over time. This is the most human element of code reviews, and therefore the hardest to automate away, but I might experiment with the following ideas as a starting point:
* a weekly briefing on the important initiatives happening in the space, what surfaces they impact, and who’s involved
* dedicated pair-programming (pair-prompting?) time between engineers to maintain opportunities to learn from each other
* retrospective reviews of code as learning exercises

## My Verdict
These purposes vary in how readily they can be automated. Quality is simply a technical problem, diversity of thought is substitutable with a writing culture, and education is nebulous but tractable.

I don’t think it’s a coincidence that the aspect of this problem that’s least obviously automatable is the most human-oriented. However, if that were the only thing holding us back from abolishing the human code review I have no doubt we’d make quick progress on it.

This leaves me somewhere between the two extremes: I don’t think the human code review is going anywhere any time soon, but I see nothing sacred about it and I expect it to gradually fade into obscurity as organizations mature towards more automation.

As for my team, I’m pushing for the quality guardrails to keep ourselves afloat amidst the flood of AI-authored changes. Maybe one day that gets us to a world without human code review, but I’m in no hurry to get there.
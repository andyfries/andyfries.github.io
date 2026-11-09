---
layout: post
title: Error Messages are the Best Context
---

Recently I was working to deprecate usages of a legacy API across a large service my team operates. I started by documenting why another API was preferred then began migrating existing callers, but new usages of the legacy API continued to appear. There was enough inertia behind the legacy pattern that humans and agents kept replicating it despite the docs. So I pivoted to an enforcement approach: existing usages get allowlisted, but any new callers on the legacy API would fail the tests and break the build. 

The enforcement approach wasn’t much harder to implement than the guidance approach I started with. The trick is that I had to know to ask for it. This is the second in a pair of posts about this topic, so I’d recommend reading [part 1]({% post_url 2026-11-08-documentation-is-a-last-resort %}) if you missed it.

<!--more-->

This same pattern is playing out across the industry. Agents make mistakes, documentation is updated, but the issues keep happening unless the behavior is enforced.

Think back to ten years ago. It was a simpler time, when you had to be a typography nerd to know the term “em dash” and emojis were rarely seen in READMEs (for projects lucky enough to have one). At that time, if an API kept getting broken by bad code changes the fix was simple: add tests. You might also improve documentation and train people more, but critical functionality had to be verified.

> When you are asking for good intentions, you are not asking for a change… because people already had good intentions. But if good intentions don’t work, what does? Mechanisms work.
> \
\
– Jeff Bezos, 2008 Amazon All Hands ([source](https://aws.amazon.com/blogs/security/how-aws-built-the-security-guardians-program-a-mechanism-to-distribute-security-ownership/))

At best, a lack of verification mechanisms limits the ability for engineers to quickly and reliably build software. At worst, lacking those mechanisms can allow bugs to be shipped and systems to fail. Both have long been true with human engineers, but the feverish pace of AI-assisted development has granted new urgency to these tradeoffs. 

Fortunately, the same trend has made it [easier than ever]({% post_url 2026-05-30-building-more-tools %}) to build enforcement mechanisms. Here are a few examples I’ve built recently:
* When changes need to be made sequentially to separate provider and consumer services, block the consumer change from merging until the provider is deployed
* Automatically run targeted integration tests on relevant changes without requiring authors to know how and when to do so
* When a PR removes a feature flag from the code, test whether that flag is actively in use

Each of these mechanisms started as documentation of best practices. Sometimes they were followed, but engineers needed to double check and that guidance wasn’t consistently applied. Now that these are deterministically verified, engineers can focus their attention on higher judgement issues.

My favorite part of this approach is that it enables self-correction. It’s essentially the codebase equivalent of [Cunningham’s Law](https://meta.wikimedia.org/wiki/Cunningham's_Law). If I try to remove an active feature flag I get a big red error describing why that’s dangerous and what I should do instead. Agents are hyper-optimized for this sort of loop so they will eagerly apply the feedback and iterate until the test passes. The result is that the behavior is deterministically enforced, humans can stop worrying about it, and agents are simultaneously more autonomous and more reliable.


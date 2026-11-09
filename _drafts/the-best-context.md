---
layout: post
title: Error Messages are the Best Context
---

Agents used to tag my teammates to review my PRs before the change was ready. Each time I’d apologize and explain it was an overzealous agent. CLAUDE.md instructions helped but sometimes got dropped or ignored. After the third time, I channeled the embarrassment and frustration into a solution: I added a [hook](https://code.claude.com/docs/en/hooks-guide) to deny the tool call that tagged people on draft PRs. 

Agents are highlighting similar process gaps at every level. But documentation isn’t a panacea. For things that matter, you need enforcement.

<!--more-->

## Documentation is a Last Resort
Tech debt has long been a fact of software engineering, but the pace of agentic development has amplified the cost of ignoring it. Critical behavior that lacked tests used to be tolerable with fewer changes flowing through the system, but now agents regularly modify that surface. Tribal knowledge that used to be sufficient in a small engineering team is now inadequate for AI-assisted contributions from outside the team. 

Documentation feels like a natural solution to protect these behaviors. Agents eagerly produce it unprompted and there’s less friction in merging those changes since docs are often seen as unobjectionable. What’s the harm in thoroughly and automatically documenting everything?

The biggest risk is that documentation can be wrong. The only thing worse than no documentation is misleading documentation, and it’s no small effort to fact-check a wall of LLM-generated text. 

Even assuming the output is accurate, this approach does a disservice to the humans in the ecosystem. [LLM writing is bad at building shared understanding]({% post_url 2026-07-18-inputs-not-outputs %}) and automatically generating a bunch of it will force any human reader to either A) spend an inordinate amount of effort to consume it or B) ignore it.

If you’re bullish on agentic engineering that may not sound like a problem. As long as agents have what they need then it doesn’t matter if humans ignore it. But this approach doesn’t work well for agents either. Having agents automatically generate system documentation is tautological: they document what they’re aware of. Putting that into agent contexts again is an exercise in redundancy. What they need is the info they can’t find.

This lesson is already enshrined in industry best practices: ‌”Document the why, not the what.” Describing a system’s burst capacity as 10X the baseline is evident from the infrastructure code; what readers need to know is that the system is used in marketing campaigns that send large bursts of scheduled traffic. That context can only come from domain experts.

Wasted context is not the only issue here. Documentation fails to even solve the original problem of protecting critical behavior. Docs can be helpful to point out information that’s undiscoverable, and they may deter misguided implementations, but the only reliable way to protect critical behaviors is to enforce them. Documentation alone cannot make guarantees, no matter how thorough your CLAUDE.md is.

## Mechanisms Over Good Intentions

It might be tempting to consider this an agentic engineering problem, that it would all go away with the right harness around the right frontier model. This is not an AI problem though: it’s a software engineering problem.

Think back ten years. It was a simpler time, when you had to be a typography nerd to know the term “em dash” and emojis were rarely seen in READMEs (for projects lucky enough to have one). At that time, if an API kept getting broken by bad code changes the fix was simple: add tests. You might also improve documentation and train people more, but critical functionality had to be enforced.

> When you are asking for good intentions, you are not asking for a change… because people already had good intentions. But if good intentions don’t work, what does? Mechanisms work.
> 
> – Jeff Bezos, 2008 Amazon All Hands ([source](https://aws.amazon.com/blogs/security/how-aws-built-the-security-guardians-program-a-mechanism-to-distribute-security-ownership/))

I was reminded of this lesson recently as I worked to deprecate usages of a legacy API across a large service my team operates. I started by documenting why another API was preferred then began migrating existing callers, but new usages of the legacy API continued to appear. There was enough inertia behind the legacy pattern that humans and agents kept replicating it despite the docs. So I pivoted: existing usages were allowlisted, but any new callers on the legacy API failed the tests and broke the build. Enforcement wasn’t much more difficult than advisement, but I had to know to look for it.

This is a mundane example but it shows the power of mechanisms. At best, a lack of verification mechanisms limits development velocity. At worst, lacking those mechanisms can allow bugs to be shipped and systems to fail. Both have long been true with human engineers, but the feverish pace of AI-assisted development has granted new urgency to the problem. 

Fortunately, the same trend has made it [easier than ever]({% post_url 2026-05-30-building-more-tools %}) to build enforcement mechanisms. Here are a few examples I’ve built:
* When changes need to be made sequentially to separate provider and consumer services, block the consumer change from merging until the provider is deployed
* Automatically run targeted integration tests on relevant changes without requiring authors to know how and when to do so
* When a PR removes a feature flag from the code, test whether that flag is actively in use

Each of these mechanisms started as documentation of best practices. They were usually followed, but engineers needed to confirm and the occasional issue slipped through. Now that these are deterministically verified and enforced, engineers can focus their attention on higher-judgement issues.

My favorite part of this approach is that it enables self-correction. It’s the codebase equivalent of [Cunningham’s Law](https://meta.wikimedia.org/wiki/Cunningham's_Law). If I try to remove an active feature flag I get a big red error describing why that’s dangerous and what I should do instead. That error message is more effective context than any documentation: it tells the reader what they need to know to resolve the problem, it’s presented only when relevant, and it’s impossible to miss because the build breaks when it comes up.

Agents are hyper-optimized for this sort of loop, so they will eagerly apply the feedback and iterate until the test passes. The result is that the behavior is deterministically enforced, humans can stop worrying about it, and agents are simultaneously more autonomous and more reliable. 

## Moving Towards Enforcement

I want to be clear that this is not a condemnation of documentation in general. Docs serve a vital function for protecting important behaviors that aren’t verifiable. The problems arise when it’s the default solution. Any verifiable behavior that’s documented without being enforced is another burden on engineers and another opportunity for things to be missed.

There are three practices that helped me consciously move towards enforcement over advisement. The first is pulled straight from the [Claude Code best practices](https://code.claude.com/docs/en/best-practices#enforce-the-rules-that-cant-have-exceptions): go through your existing CLAUDE.md (or equivalent) and look for phrases like “never”, “always”, or “don’t touch”. These are all great candidates for enforcement. Ask an agent to migrate a few into hooks, tests, or permissions and get a feel for the workflow. Watch for any friction that will impede enforcement mechanisms (e.g. the codebase isn’t set up for linting rules) and prioritize removing it.

The next practice is that I ask “what mechanisms could have prevented this” whenever something goes wrong with the system or my dev workflows. I don’t mean that figuratively; I literally ask an agent that question and often build the resulting suggestions. This is a post-mortem practice writ small. Because the cost of code has dropped precipitously, the same mindset previously reserved for large incidents can now be applied all the way down the stack to something as trivial as preventing reviewers from being tagged on draft PRs.

Finally, I have a scheduled routine that scans my environment once a week to look for enforcement opportunities. The routine looks at Slack, PRs, and my agent sessions to identify areas requiring [toil](https://sre.google/sre-book/eliminating-toil/). This routine has recommended improvements based on recurring PR feedback, common questions I ask agents, and performance investigations shared on Slack.

Together these practices enable continuous improvement grounded in verifiable behavior. Given enough time and ambition, that’s a force that can reshape an engineering organization. It all starts with an error message on an undesirable tool call.
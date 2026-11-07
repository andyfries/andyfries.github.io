---
layout: post
title: Documentation is a Last Resort
---

Agents used to tag my teammates to review my PRs before the change was ready. Each time I’d apologize and explain it was an overzealous agent. CLAUDE.md instructions helped but sometimes got dropped or ignored. After the third time, I channeled the embarrassment and frustration into a solution: I added a [hook](https://code.claude.com/docs/en/hooks-guide) to deny the tool call that tagged people on draft PRs. 

Across the industry, agents are highlighting similar gaps at every level. But documentation isn’t a panacea.

<!--more-->

Tech debt has long been a fact of software engineering, but the pace of agentic development has amplified the cost of ignoring it. Critical behavior that lacked tests used to be tolerable with fewer changes flowing through the system, but now agents regularly modify that surface. Tribal knowledge that used to be sufficient in a small engineering team is now inadequate for AI-assisted contributions from outside the team. 

Documentation feels like a natural solution. Agents eagerly produce it unprompted and there’s less friction in merging those changes since docs are often seen as unobjectionable. What’s the harm in thoroughly and automatically documenting everything?

The biggest risk is that documentation can be wrong. The only thing worse than no documentation is misleading documentation, and it’s no small effort to fact check a wall of LLM-generated text. 

Even assuming the output is accurate, this approach does a disservice to the humans in the ecosystem. [LLM writing is bad at building shared understanding]({% post_url 2026-07-18-inputs-not-outputs %}) and automatically generating a bunch of it will force any human reader to either A) spend an inordinate amount of effort to consume it or B) ignore it.

If you’re bullish on agentic engineering that may not sound like a problem. As long as agents have what they need then it doesn’t matter if humans ignore it. But this approach doesn’t work well for agents either. Having agents automatically generate system documentation is tautological: they document what they’re aware of. Duplicating this information into documentation only pollutes context. What they need is the information they can’t discover.

This is a lesson already enshrined in best practices: ‌”Document the why, not the what.” Describing a system’s burst capacity as 10X the baseline is evident from the infrastructure code; what readers need to know is that the system is used in marketing campaigns that send large bursts of scheduled traffic. That context can only come from domain experts.

The potential cost here is not only wasted context. Documentation fails to solve the original problem of protecting the critical aspects of the system. It can be helpful to describe undiscoverable behavior, and it may deter misguided implementations, but the only reliable way to protect the critical aspects of the system is to verify them. Documentation alone cannot accomplish that, no matter how thorough your CLAUDE.md is.

In contrast, verifiable protections can unlock more autonomous agentic loops. Documenting that new callers shouldn’t consume a legacy API is helpful, but adding a CI job that breaks the build when that happens reliably steers humans and agents towards the right behavior.

This yields three criteria for writing documentation: the issue is important, not discoverable, and not verifiable. If the issue isn’t important then the costs of documenting it aren’t worthwhile. If the issue is discoverable then documentation isn’t necessary. If the issue is verifiable, then it can be enforced rather than merely documented. See part 2 - *Error Messages are the Best Context* for more on that.
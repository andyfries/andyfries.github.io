---
layout: post
title: You Should be Building More Tools
---

The cost of writing code is plummeting. That's good for shipping more features, but it's even better for building more tools.

<!--more-->

METR published a [graph](https://metr.org/time-horizons/) of the length of software tasks LLMs can complete that absolutely fascinates me. With length of time as a rough proxy for complexity, this is the single best visual I've found to quantify a trend I've experienced qualitatively over the past two years: the cost of writing software is rapidly shrinking.

This trend is at the heart of so many hot-button issues in the industry today -- PR slop, layoffs in the name of increased productivity, the death of craftsmanship in code, the idea of a one-person unicorn startup, etc. 

There's a lot to dislike here. We're only beginning to understand how this will turn our world upside-down, and a lot of it isn't looking good. But as a matter of principle and mental well-being, I'm choosing to focus on the opportunities being created. For my role as a software engineer responsible for building user-facing products the clearest opportunity is the ability to ship more features. Much has been said on that topic already though, so I'd like to highlight a less obvious opportunity.

**You should be building more tools.**

Take a minute to reflect on the technical landscape you operate in. How often are you performing repetitive processes, tolerating inconveniences tangential to your work, or fighting against unintuitive interfaces that don't match your workflows? When was the last time you really evaluated what it would cost to build or improve tools to solve those problems?

I'd guess the cost is a lot lower than it was, even just a few months ago. For most feature development the cost of writing code is a small fraction of the total cost; processes like product alignment, QA, localization, and legal review usually make up the majority of development timelines. Tooling rarely requires that overhead though. As a set of problems that are bottlenecked by pure code, tools are uniquely positioned to benefit from the shrinking cost.

This is the [personal software revolution](https://www.theverge.com/tech/928905/vibe-code-personal-software-revolution) in an enterprise context. As inspiration, here are a few examples of the types of tools I've built this year:
* PR review dashboard - tailored to my workflow so I can track exactly where my attention is needed
* Observability events - instrumented my team's main application to surface key debugging info to oncalls through a convenient UI
* Home Assistant automation - configures my office lighting when I join a Zoom call

None of these are revolutionary ideas. All of them have been possible to implement for years, but the upside was never worth the work it would take to get there. The critical difference now is that the investment portion of the ROI equation has dropped dramatically. A whole class of tools suddenly moved from unjustifiable to worthwhile in the past year. The hard part now is fighting the cognitive inertia to actually notice that shift.


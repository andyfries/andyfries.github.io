---
layout: post
title: Reviewing Code
---

My code review approach is one simple question: is it easy to read?

<!--more-->

Early in my career I was advised to develop my coding skills by reading the source code for a popular project like the Linux kernel or Redis and I was disappointed to get nothing from it. I'd spend a while trying to perceive the technical lessons that supposedly awaited me in those codebases only to end up frustrated and none the wiser.

Thankfully, I stumbled across another way to improve: code reviews. Many of my coworkers would rubber stamp my review requests, but a handful of the more senior (read: opinionated) engineers would thoroughly mark up my changes with references to principles and patterns I’d never heard of. Their ability to find opportunities for simplification was humbling. In time I internalized these lessons and developed my own sense of how to write good code.

As I got more experience and moved into mentorship roles, my thoughts increasingly turned towards reading code rather than writing it. How could I live up to the example those senior engineers had set for me with their encyclopedic knowledge of design patterns and SOLID principles they’d used to find improvements in my code?

Trying to emulate their results didn’t work. Reading _[Gang of Four](https://en.wikipedia.org/wiki/Design_Patterns)_ and _Clean Code_ brought back memories of trying to read the Redis codebase; I learned little except about my own inadequacy. When I managed to actually remember one of these concepts, I didn’t have any intuition for when to apply it.

One thing I did have as a reviewer was a willingness to admit ignorance or confusion. If I didn’t understand something, I’d ask the author to explain it. Over time I realized this habit had a knack for finding opportunities to simplify. I’d accidentally discovered an alternate path to giving quality code reviews, one that didn’t require thorough academic knowledge.

I decided to commit to this approach. I made readability my guiding principle in reviewing code, paying special attention to anything that improved or hindered the reading experience. The value of this might seem dubious until you consider how many “best practices” can be reframed as readability problems. 

For example, the [single responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle) is an oft-cited guideline for better cohesion in classes, but it also speaks to a readability issue: is it easier to read an implementation doing one thing or a variety of things? The [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle) can be reframed as the [principle of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment): it’s less confusing when subclasses are consistent with parent behavior. The [DRY principle](https://en.wikipedia.org/wiki/Don't_repeat_yourself) can be helpful for minimizing the surface area for potential bugs, but it also gives readers an explicit indication that the same thing is happening in multiple places.

My review process is a collection of these heuristics:
- If I have to reread a function repeatedly before I understand it, that's a sign something about it is subtle, unintuitive, or overly complex. 
- If I get confused about where I'm at in a class with multiple similar methods, that's a sign their use isn't distinct enough. 
- If I'm surprised by the usage of a variable, that's a sign its scope or name isn't obvious. 
- If I see the same pattern in multiple classes without a unifying structure that makes it apparent, that's a sign an abstraction like inheritance or composition might be needed to communicate the pattern to readers.

Here’s an example:
```java
public class AuditInfo {
  private Map<String, String> fields = new HashMap<>();

  public void addUserInfo(User user) {
    fields.put("name", user.getName());
    fields.put("userId", user.getId());
  }
  
  public void addTripInfo(Trip trip) {
    fields.put("tripId", trip.getId());
    fields.put("tripStartTime", trip.getStartTime());
  }
}
```

What’s striking about this snippet? For me it’s the similarity between the two `add` methods. Both look like they’re doing roughly the same thing but there’s nothing in the code to enforce that. This prompts me to read each one carefully to examine the differences between the two. That careful reading is a point of friction for the reader, and now we have a useful piece of feedback:

> I notice we have multiple `add` methods doing almost the same thing. Can we do something to make that pattern more explicit?

In similar cases I’ve noticed that interfaces can be useful to encapsulate repetition, so let’s see what that looks like:
```java
public interface Auditable {
  Map<String, String> getAuditInfo();
}

public class AuditInfo {
  private Map<String, String> fields = new HashMap<>();
  
  public void add(Auditable auditable) {
    fields.putAll(auditable.getAuditInfo());
  }  
}


public class User implements Auditable {
  @Override
  public Map<String, String> getAuditInfo() {
    Map<String, String> fields = new HashMap<>();
    fields.put("name", this.getName());
    fields.put("userId", this.getId());
    return fields;
  }
}


public class Trip implements Auditable {
  @Override
  public Map<String, String> getAuditInfo() {
    Map<String, String> fields = new HashMap<>();
    fields.put("tripId", this.getId());
    fields.put("tripStartTime", this.getStartTime());
    return fields;
  }
}
```

This creates a more extensible solution with better cohesion. `AuditInfo` doesn’t have to keep track of all the relevant fields for every auditable type which will keep it simple as the number of audited types grows.

This approach works at any experience level. Junior engineers can point out where they got confused while more experienced engineers can go further and suggest specific solutions. Even without deep technical knowledge, merely pointing out friction for the reader can create an opportunity to collaboratively improve it.

Besides being accessible, the main reason to review for readability is that it’s incredibly effective. I often hear that my code reviews are unusually substantive and useful, especially in architectural areas, but even my most technical feedback starts with my experience as a reader.

You don't need deep formal knowledge of software engineering principles to give great code reviews. Next time you're reviewing a change, ask yourself: is it easy to read? You'll be surprised how much that question reveals.
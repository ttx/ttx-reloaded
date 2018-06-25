Title: A framework for lightweight open source governance
Date: 2018-06-25 13:45
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: lightweight-governance-framework

Any group of humans needs some form of governance. It’s a set of rules
the group follows in order to address issues and take clear decisions.
Even the absence the rules (anarchy) is a form of governance! At the
opposite end of the spectrum is dictatorship, where all decisions are
made by one person. Open source projects are groups of humans, and they
are no exception to this. They can opt for various governance models,
which I detailed in a
[previous article](https://ttx.re/foss-project-governance-models.html)
four years ago (how time flies!).

That [article](https://ttx.re/foss-project-governance-models.html) compared
various overall models in terms of which one would best ensure the long-term
survival of the community, avoiding revolutions (or forks). It advocated for
a representative democracy model, and since then I've been asked several
times for the best recipe to implement it. However there are numerous
trade-offs in the exercise of building governance, and the "best" depends
a lot on the specifics of each project situation. So, rather than detail a
perfect one-size-fits-all governance recipe, in this article I'll propose a
framework of three basic rules to keep in mind when implementing it.

This simple 3-rule model can be used to create **just enough** governance,
a lightweight model that should be sustainable over the long run, while
avoiding extra layers of useless bureaucracy.

### Rule #1: Contributor-driven bodies

Governance bodies for an open source project should be selected by the
contributors to the project. I'm not talking of governance bodies for
open source Foundations (which generally benefit from having some
representation of their corporate sponsors chiming in on how their
money shall be spent). I'm talking about the upstream open source project
itself, and how the technical choices end up being made in a community of
contributors.

This rule is critical: it ensures that the people contributing code,
documentation, usage experience, mentoring time or any other form of
contribution to the project are aligned with the leadership of the
project. When this rule is not met, generally the leadership and the
contributors gradually drift apart, to the point where the contributors
no longer feel like their leadership represents them. This situation
generally ends with contributors making the disruptive decision to fork
the project under a new, contributor-aligned governance, generally leaving
the old governance body with a trademark and an empty shell to govern.

One corollary of that first rule is that the governance system must
regularly allow replacement of current leaders. Nobody should be appointed
for life, and the contributors should regularly be consulted, especially
in fast-moving communities.

### Rule #2: Aligned with their constituencies

This is another corollary of the first rule. In larger projects, you need
enough governance bodies to ensure that each is aligned with its own
constituency. In particular, if your community is made of disjoint groups
with little to no overlap in membership, and those groups each need decisions
to be made, they probably need to each have their own governance body at that
level.

The risk we are trying to avoid here is dominance of the larger group over
smaller groups. If you use a single governance body for two (or more)
disjoint groups, chances are that the larger group will dominate the
representative governance body, and therefore will end up making decisions
for the smaller group. This is generally OK for global decisions that affect
every contributor equally, but matters that are solely relevant to the
smaller group should be decided at the smaller group level, otherwise that
group might be tempted to fork to regain final call authority over their
own things.

### Rule #3: Only where decisions are needed

Strict application of rule #2 tends to result in the creation of a large
number of governance bodies, that's why you need to balance it with rule #3:
only create governance bodies where decisions are actually needed. The art
of lightweight governance is, of course, to find the best balance between
rule #2 and rule #3.

This rule has two practical consequences. The first one is obvious: you should
not create vanity governance bodies, just to give people or organizations a
cool title or badge. Numerous communities fall in the trap of creating
"advisory" boards with appointed seats, to thank long-standing community
members, or give organizations the illusion of control. Those bodies create
extra bureaucracy while not being able to make a single call, or worse,
trying desperately to assert authority to justify their existence.

The second consequence is, before creating a governance body at a certain
level in the project organization, you should question whether decisions
are really needed at that level. If the group needs no final call, or can
trust an upper decision body to make the call if need be, maybe that
governance body is not needed. If two governance bodies need to cooperate
to ensure things work well between them, do you really need to create a
governance body above them, or just encourage discussion and collaboration ?
This trade-off is more subtle, but generally boils down to how badly you
need final decisions to be made, vs. letting independently-made decisions
live alongside.


That is all there is to it! As I said in the introduction, those three
rules are not really a magic recipe, but more of a basic framework to
help you, in the specific situation of your community, build healthy
communities with *just enough* governance. Let me know if you find it useful!


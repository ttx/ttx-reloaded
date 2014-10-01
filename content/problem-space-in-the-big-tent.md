Title: The problem space in the big tent
Date: 2014-10-01 14:39
Author: Thierry Carrez
Tags: OpenStack
Slug: problem-space-in-the-big-tent


Unless you have been living under a rock, you must have noticed that the
OpenStack community is [currently](https://dague.net/2014/08/26/openstack-as-layers/) [brainstorming](http://inaugust.com/post/108) [potential](http://www.joinfu.com/2014/09/so-what-is-the-core-of-openstack/) [evolutions](http://www.stillhq.com/openstack/kilo/000002.html)
to its project and governance structure. A lot of those posts focused on
solutions and implementation details, and it's easy to design the wrong
solution when you didn't first define the problem space. So in this post I'd
like to take a step back and look at which issues are we trying to solve, and
the constraints we have.

With the continued growth of OpenStack, the current project structure and
governance model (which you can largely blame me for) fail in various ways.

### The "integrated release" Grail

In our current structure, the integrated release is the ultimate goal, with
being recognized as an official program and being incubated seen as the first
steps in the enlightenment ladder. That creates a number of issues.

First, the integrated release being the ultimate goal, there is no lack of
candidate projects, and it is always-growing. Why reject Sahara if you
accepted Trove ? However, processes and services are applied equally to all
members of the integrated release: we gate everything in the integrated
release against everything else, we do a common, time-based release every
6 months, we produce documentation for all the integrated release components,
etc. The resources working on those integrated horizontal tasks are very
finite, and complexity grows non-linearly as we add more projects. So there
is outside pressure to add more projects, and internal pressure to resist
further additions. This is obviously not sustainable.

Second, projects outside the integrated release fail to get the recognition
they deserve. Some companies won't invest resources to participate in a
"non-official" project. So becoming part of the integrated release, which
was designed to be a technical decision, quickly became a life-or-death
question for new projects, and a political/community minefield.

We need to find a model that lets us be inclusive of all "OpenStack" projects,
while preserving the resources of the horizontal teams. I think Monty's
"layer #1" (which I prefer to call **Ring0**) solves that issue, by defining
a user-case-driven, limited, mostly-static set that the current horizontal
teams (infra, release management, QA, Docs...) can commit to supporting
directly. All the other projects may or may not be supported directly (or
just getting tools and advice to do it themselves), depending on those
horizontal teams capacity. By making ring0 arbitrarily small and static, most
things would not be in it, so we avoid the Grail effect. Projects outside
ring0 can enjoy more freedom (with their release cycle, with their gating
choices...) than the tightly-controlled ring0. Ring0 becomes a production
artifact, not a badge of honor.

### Duplication, Competition and Overlap

In the early days of this project, I was obsessed with avoiding duplication
of effort. In a large project like OpenStack, it's really easy for teams to
work in their (usually corporate) corner on their own invented-here solution
for a common problem. So the governance model was built to reduce the risk of
duplication of effort, by creating obviously-blessed projects, obsessively
avoiding overlap in scope, and constantly encouraging people to merge their
work and join existing teams rather than do their own thing. We could say it
was quite successful, and whoever has attended our Design Summits can see
how this cross-organization collaboration miracle happens every time.
Some take it now for granted, but it didn't happen by accident. 

That said, there is now the unintended side-effect that we actively prevent
the emergence of better alternatives to replace existing "blessed" things.
It's currently difficult for a project to prove itself outside an official
program, in the shadow of an existing project with the "integrated" badge.

It's a difficult balance to strike. We still mostly want to avoid duplication
of effort and have teams cooperate and join efforts on the same code base,
since avoiding such waste is one of the big benefits of our open source/open
design/open development model. But we still want to let new flowers bloom.
I hope that removing blessed programs and the ladder to integrated will go
a long way to fix this, but I'd hate it if we ended up discouraging
collaboration as a side effect.

We also need to keep discouraging partially-overlapping scopes, because that
would be a disservice to our users. If a project does AB and another does CD,
there is little value to our users in a new project that would do ABC.

### Not answering the right questions

The last issue with the current system is that it fails to answer the
questions that our downstream users (packagers, deployers, end users) rightly
ask themselves about OpenStack. A single, binary badge of honor just can't
answer all the different questions. Jay's
[post](http://www.joinfu.com/2014/09/so-what-is-the-core-of-openstack/)
touches on that part extensively: I think developing a tag taxonomy to
document what each project in "OpenStack" can do for you, depending on what
type of user you are, is a good answer. Removing the "integrated release"
super-badge will allow that information to emerge.

### The limit of the tent

So it's quite obvious at this point that we need to change the concept of
"integrated release", which is a lot too binary. Replacing it with a set of
flexible structures (a tag taxonomy, a ring0 that current horizontal teams in
OpenStack feel fine supporting, other groups as needed...) sounds like the
way to go. Being inclusive in what we accept in the "big tent" is also very
consensual. But even big tents have limits, lines in the sand that we draw
between what is in and what is not in. Where should be ours ? Supporters of
the big tent approach all seem to diverge on that detail.

There is still a marginal cost to pay for each project we add. If we decide
to precisely describe projects in the OpenStack ecosystem using a set of tags,
as Jay suggested, then it's only valuable if it's kept current, and the
maintenance cost increases (linearly) with each project addition. If those
projects are to be called "OpenStack", they may trigger a trademark search,
too. And what about Design Summit space ?

I'd like projects to at very least loosely align with the OpenStack mission,
otherwise we'd lose our key identity and purpose. Monty proposes an alignment
check ("are you one of us"), which mostly translates into observing a number
of key governance and technical principles. He would also focus design summit
space on "Ring0" projects. I fear that may make Ring0 artificially attractive
and recreate a Grail effect, but I don't have a better solution to suggest.

### The TC constituency

The last constraint would be to find the right constituency for the Technical
Committee. The Technical Committee is defined in the Foundation bylaws as the
governance body in charge of the technical direction of "OpenStack" as a whole.
There is an essential symmetry, where projects willingly place themselves
under the authority of the TC, and in exchange get the right to participate
in the Technical Committee members election. We used to do that by blessing
individual projects. Currently we bless teams instead (the "Programs" concept
was created to add a level of indirection between the team we bless and the
code repositories they want to work on, to give teams more flexibility on how
they organize their code). As we change the structure, we need to find what
the new area of authority of the TC is, and therefore what its new
constituency would look like.

There are two approaches. You can consider that the TC only has authority
over a subset (Ring0) and supporting projects (horizontal efforts which
apply to Ring0). But that kind of mean other projects are not really
"OpenStack". The other approach is to consider that all the "big tent" is
under the authority of the Technical Committee, and contributing to any
project in the big tent gives you a right to vote in TC membership elections.
I'm leaning toward the latter option, even if that will change the dynamics
of the TC and may require stronger alignment checks ("are you one of us")
before entry.

### Conclusion

As we move on and prepare more detailed proposals, I'd like to make sure all
the proposed solutions have an answer for those various questions:

1. How do we solve the integrated gate bottleneck ?
1. How do we solve the horizontal teams scaling issues ?
1. How do we prevent having a single Grail, to move the TC away from its
   current badge-granting authority role ?
1. How do we allow competition and alternative solutions ?
1. How do we continue to encourage collaboration and avoid duplication of
   effort ?
1. How do we keep on discouraging partial scope overlap ?
1. How do we provide the answers about our projects that our
   packagers/deployers/endusers are needing ?
1. If a "big tent" approach is proposed, where does the big tent end ?
1. What would the Design Summit look like in the new world order ?
1. What would the TC area of authority (and therefore constituency) be in
   the new world order ?

Now, brainstorm on.

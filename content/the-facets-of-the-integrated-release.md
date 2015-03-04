Title: The facets of the OpenStack integrated release
Date: 2015-03-04 16:00
Author: Thierry Carrez
Tags: OpenStack
Slug: facets-of-the-integrated-release


In a recent [Technical Committee update](http://www.openstack.org/blog/2015/02/tc-update-project-reform-progress/) on the OpenStack blog,
I explained how the OpenStack "integrated release" concept, due to its binary
nature, ended up meaning all sorts of different things to different people.
That is the main reason why we want to deconstruct its various meanings into
a set of tags that can be independently applied to projects, in order to more
accurately describe our project ecosystem.

In this blogpost, I'll look into the various meanings the "integrated release"
ended up having in our history, and see how we can better convey that
information through separate tags.


## Released together

The original meaning of "integrated release" is that all the projects in it
are released together on the same date, at the end of our development cycles.

I recently [proposed](https://review.openstack.org/#/c/157322/) a tag
("release:at-6mo-cycle-end") to describe projects that commit to producing
a release at the end of our development cycles, which I think will cover
that facet.


## Managed release

Very quickly, the "integrated release" also described projects which had their
release managed by the OpenStack Release Management team. This team sets up
processes (mostly a
[Feature Freeze](https://wiki.openstack.org/wiki/FeatureFreeze)
deadline and a
[release candidate dance](https://wiki.openstack.org/wiki/Release_Cycle#Pre-release_.28Release_Candidates_dance.29))
to maximize the chances that managed projects would release on a pre-announced
date, and that none of the managed projects would end up delaying the end
release date.

Projects would be added to incubation and when we thought they were ready to
follow those processes without jeopardizing the "integrated release" for
existing projects, they would get added to be the next release.

That is a separate facet from the previous one, so I
[proposed](https://review.openstack.org/#/c/157322/) a separate tag
("release:managed") to describe projects that happen to still be handled by
the Release Management team.


## Co-gating

As we introduced complex code gating in OpenStack Infrastructure, the
"integrated release" concept grew another facet: it would also mean that
projects changes are tested against one another master branches. That way
we ensure that changes in project B don't break project A. This is rather
neat for a tightly-coupled set of projects. But this may be a bit overkill
for projects higher in the stack that just consume public APIs. Especially
when non-deterministic test errors in project A prevent changes from landing
in B.

We need to revise how to split co-gating in meaningful groups.
[This work](https://review.openstack.org/#/c/150653/) is led by Sean Dague.
Once it is completed, I expect us to convey the information on what is
actually tested together using tags as well.


## Supported by OpenStack horizontal efforts

From there, the "integrated release" naturally evolved to also being the set
of projects that horizontal efforts (such as Documentation, QA, stable branch
maintenance, Vulnerability management, Translations...) would focus their
work on. Being part of the "integrated release" ensured that you would get
fully supported by those horizontal teams.

That didn't scale that well, though. The documentation team was the first to
exhaust their limited resources, and started to move to a model where they
would not directly write all the docs for all the integrated projects. Since
then, all horizontal teams decided to gradually move to the same model, where
they would directly handle a number of projects (or none), but provide tooling,
mentoring and support for all the others.

It's still valuable information to know which project happens to be directly
handled by which horizontal effort, and which project ends up having security
support or basic docs. So we'll introduce tags in the future to accurately
describe this facet.


## The base features

Going downhill, the "integrated release" started to also mean the base
features you can rely on being present when people say they deployed
"OpenStack". That was a bit at odds with the previous facets though: why would
all co-gating projects with a coordinated release necessarily be essential ?
And indeed, the integrated release grew beyond "base" features (like Keystone)
to include obviously optional projects (like Sahara or Ceilometer).

I personally think our users would still benefit from a description of what
layer each project belongs to: is it providing base IaaS compute functionality,
or is it relying on that being present ? This is not a consensual view though,
as some people object to all proposals leading to any type of ranking within
OpenStack projects.


## OpenStack

At that point, the "integrated release" was "the OpenStack release", and things
outside of it were "not OpenStack".

This obviously led to more pressure to add more projects in it. But when the
OpenStack governance (previously under a single Project Policy Board
banner) was split between the Technical Committee and the Foundation Board,
the former retained control over the "integrated release" contents, and the
latter took control of trademark usage. This created tension over that specific
facet.

Defcore was created to solve this problem, by defining the criteria to apply
to various trademark programs. When asked to provide a set of projects (or
rather, as set of sections of code) to apply the trademark on, the Technical
Committee answered with the only concept it had (you guessed it, "the
integrated release" again).

In the tags world, when asked for a set of projects to apply a particular
trademark program to, the Technical Committee shall be able to provide a
finer-grained answer, by defining a specific tag for each question.


## Stability

Further downhill, "integrated release" also started to mean "stable". Once
published in such a release, a project would not remove a feature without
proper discussion, notice, and deprecation period. That was yet another
facet of the now-bloated "integrated release" concept.

The issue is, all projects were not able to commit to the same stability
rules. One would never deprecate an existing feature, while one would rip
its API off over the course of two development cycles. One size didn't fit
all.

In the tags world, my view is that Ops and devs, working together, should
define various stability levels and the rules that apply for each. Then each
project can pick the tag corresponding to the stability level they can commit
to.


## Maturity

Last but not least, at one point people started to assume that projects in
the "integrated release" were obviously mature. They were all in widespread
usage, enterprise-ready, carrier-grade, service-provider-class, web-scale.
The reality is, this facet is also complex: some projects are, and some
projects are less, and some projects aren't. So we need to
describe the various maturity styles and levels, and inform our users of each
project real status.

It's difficult to describe maturity objectively though. I intend to discuss
that topic with the ones that are the best placed to accurately describe it:
the OpenStack operators gathered at the Ops Summit next week.

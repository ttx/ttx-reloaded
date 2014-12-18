Title: The Way Forward
Date: 2014-12-18 14:15
Author: Thierry Carrez
Tags: OpenStack
Slug: the-way-forward

The OpenStack project structure has been under heavy discussion over the
past months. There was a
[long email thread](http://lists.openstack.org/pipermail/openstack-dev/2014-August/041929.html),
[a](https://dague.net/2014/08/26/openstack-as-layers/)
[lot](http://inaugust.com/post/108)
[of](http://www.stillhq.com/openstack/kilo/000002.html)
[opinionated](http://ttx.re/problem-space-in-the-big-tent.html)
[blogposts](http://www.joinfu.com/2014/09/so-what-is-the-core-of-openstack/),
a [cross-project design summit session](https://etherpad.openstack.org/p/kilo-crossproject-growth-challenges)
in Paris, and various strawmen proposed to our
[governance repository](https://review.openstack.org/#/q/project:openstack/governance,n,z).
Based on all that input, the OpenStack Technical Committee worked on a clear
specification of the problems we are trying to solve, and the proposed way
to fix them. What follows is an excerpt of the
[approved resolution](https://review.openstack.org/#/c/138504/).


## Problem description

Our project structure is currently organized as a ladder. Developers form
teams, work on a project, then apply for incubation and ultimately graduate
to be part of the OpenStack integrated release. Only integrated projects
(and the few horizontal efforts necessary to build them) are recognized
officially as "OpenStack" efforts. This creates a number of issues, which
were particularly visible at the Technical Committee level over the Juno
development cycle.

First, the integrated release as it stands today is not a useful product for
our users. The current collection of services in the integrated release spans
from cloud native APIs (swift, zaqar in incubation), base-level IaaS blocks
(nova, glance, cinder), high-level aaS (savana, trove), and lots of things
that span domains. Some projects (swift, ironic...) can be used quite well
outside of the rest of the OpenStack stack, while others (glance, nova)
really don't function in a different context. Skilled operators aren't
deploying "the integrated release": they are picking and choosing between
components they feel are useful. New users, however, are presented with a
complex and scary "integrated release" as the thing they have to deploy and
manage: this inhibits adoption, and this inhibits the adoption of a slice of
OpenStack that could serve their need.

Second, the integrated release being the only and ultimate goal for projects,
there is no lack of candidates, and the list is always-growing. Why reject
Sahara if you accepted Trove? However, processes and services are applied
equally to all members of the integrated release: we gate everything in the
integrated release against everything else, we do a common, time-based
release every 6 months, we produce documentation for all the integrated
release components, etc. The resources working on those integrated horizontal
tasks are very finite, and complexity grows non-linearly as we add more
projects. So there is outside pressure to add more projects, and internal
pressure to resist further additions.

Third, the binary nature of the integrated release results in projects
outside the integrated release failing to get the recognition they deserve.
"Non-official" projects are second- or third-class citizens which can't get
development resources. Alternative solutions can't emerge in the shadow of
the blessed approach. Becoming part of the integrated release, which was
originally designed to be a technical decision, quickly became a
life-or-death question for new projects, and a political/community minefield.

In summary, the "integrated release" is paradoxically too large to be
effectively integrated, installed or upgraded in one piece, and too small to
express the diversity of our rich ecosystem. Its slow-moving, binary nature
is too granular to represent the complexity of what our community produces,
and therefore we need to reform it.

The challenge is to find a solution which allows to address all those three
issues. Embrace the diversity of our ecosystem while making sure that what
we produce is easily understandable and consumable by our downstream users
(distributions, deployers, end users), all that without putting more stress
on the already overworked horizontal teams providing services to all
OpenStack projects, and without limiting the current teams access to common
finite resources.


## Proposed change

### Provide a precise taxonomy to help navigating the ecosystem

We can't add any more "OpenStack" projects without dramatically revisiting
the information we provide. It is the duty of the Technical Committee to
help downstream consumers of OpenStack understand what each project means
to them, and provide them with accurate statuses for those projects.

Currently the landscape is very simple: you're in the integrated release, or
you're not. But since there was only one category (or badge of honor), it
ended up meaning different things to different people. From a release
management perspective, it meant what we released on the same day. From a
CI perspective, it meant what was co-gated. From an OpenStack distribution
perspective, it meant what you should be packaging. From some operator
perspective, it meant the base set of projects you should be deploying. From
some other operator perspective, it meant the set of mature, stable projects.
Those are all different things, and yet we used a single category to describe
it.

The first part of the change is to create a framework of tags to describe
more accurately and more objectively what each project produced in the
OpenStack community means. The Technical Committee will define tags and the
objective rules to apply them. This framework will allow us to progressively
replace the "integrated release" single badge with a richer and more nuanced
description of all "OpenStack" projects. It will allow the Technical
Committee to provide more precise answers to the Foundation Board of
Directors questions about which set of projects may make sense for a given
trademark license program. It will allow our downstream users to know which
projects are mature, which are security-supported, which are used in more
than one public cloud, or which are really massively scalable.

### Recognize all our community is a part of OpenStack

The second part of the change is recognizing that there is more to
"OpenStack" than a finite set of projects blessed by the Technical
Committee. We already have plenty of projects that are developed on
OpenStack infrastructure, follow the OpenStack way of doing things, have
development discussions on the openstack-dev mailing-list and
use #openstack-meeting channels for their team meetings. Those are part of
the OpenStack community as well, and we propose that those should considered
"OpenStack projects" (and be hosted under openstack git namespaces), as
long as they meet an objective criteria for inclusion (to be developed as one
of the work items below). This might include items such as:

* They align with the OpenStack Mission: the project should help further the
  OpenStack mission, by providing a cloud infrastructure service, or
  directly building on an existing OpenStack infrastructure service

* They follow the OpenStack way: open source (licensing), open community
  (leadership chosen by the contributors to the project), open development
  (public reviews on Gerrit, core reviewers, gate, assigned liaisons), and
  open design (direction discussed at Design Summit and/or on public forums)

* They ensure basic interoperability (API services should support at least
  Keystone)

* They submit to the OpenStack Technical Committee oversight

These criteria are objective, and therefore the Technical Committee may
delegate processing applications to another team. However, the TC would
still vote to approve or reject applications itself, based on the
recommendations and input of any delegates, but without being bound to
that advice. The TC may also decide to encourage collaboration between
similar projects (to reduce unnecessary duplication of effort), or to
remove dead projects.

This proposed structure will replace the current program-driven structure.
We'll still track which team owns which git repository, but this will let
multiple different "OpenStack" teams potentially address the same problem
space. Contributors to projects in the OpenStack git namespace will all be
considered ATCs and participate in electing the Technical Committee.

### Transition

As for all significant governance changes, we need to ensure a seamless
transition and reduce the effect of the reform on the current development
cycle. To ensure this seamless transition, the OpenStack taxonomy will
initially define one tag, "integrated-release", which will contain the
integrated projects for the Kilo cycle. To minimize disruption, this tag
will be used throughout the Kilo development cycle and for the Kilo end
release. This tag may be split, replaced or redefined in the future, but
that will be discussed as separate changes.

## Next steps

I invite you to read
[the full text](http://governance.openstack.org/resolutions/20141202-project-structure-reform-spec.html)
of this Technical Committee resolution to learn more about the proposed
implementation steps or the impact on current projects.

It's important to note that most of the work and decisions are still ahead of
us: those proposed changes are just the base foundational step, enabling the
future evolution of our project structure and governance. Nevertheless, it
still is a significant milestone to clearly describe the issues we are
working to solve, and to agree on a clear way forward to fix those.

The next step now is to communicate more widely about the direction we are
going, and start the discussion on some more difficult and less consensual
details (like the exact set of objective rules applied to judge new entrants,
or the need - and clear definition for - a *compute-base* tag).

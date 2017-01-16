Title: So you want to create a new official OpenStack project...
Date: 2017-01-16 14:00
Author: Thierry Carrez
Tags: OpenStack
Slug: create-official-openstack-project

OpenStack development is organized around a mission, a
[governance model](https://governance.openstack.org/tc/reference/charter.html)
and a [set of principles](https://governance.openstack.org/tc/reference/principles.html).
Project teams apply for inclusion, and the
*[Technical Committee](https://governance.openstack.org/tc/)* (TC),
elected by all OpenStack contributors, judges whether that team work helps
with the OpenStack mission and follows the OpenStack development principles.
If it does, the team is considered part of the OpenStack development
community, and its work is considered an official OpenStack project.

The main effect of being official is that it places the team work under the
oversight of the Technical Committee. In exchange, recent contributors to that
team are considered
*[Active Technical Contributors](https://governance.openstack.org/tc/reference/charter.html#voters-for-tc-seats-atc)*
(ATCs), which means they can participate in the vote to elect the Technical
Committee.

### Why ?

When you want to create a new official OpenStack project, the first thing to
check is whether you're doing it for the right reasons. In particular, there
is no need to be an official OpenStack project to benefit from our outstanding
project infrastructure (git repositories, Gerrit code reviews, cloud-powered
testing and gating). There is also no need to place your project under the
OpenStack Technical Committee oversight to be allowed to work on something
related to OpenStack. And the ATC status no longer brings additional benefits,
beyond the TC election voting rights.

From a development infrastructure standpoint, OpenStack provides the
governance, the systems and the neutral asset lock to create open
collaboration grounds. On those grounds multiple organizations and
individuals can cooperate on a level playing field, without one
organization in particular owning a given project.

So if you are not interested in having new organizations contribute to your
project, or would prefer to retain full control over it, it probably makes
sense to **not** ask to become an official OpenStack project. Same if you
want to follow slightly-different principles, or want to relax certain
community rules, or generally would like to behave a lot differently than other
OpenStack projects.

### What ?

Still with me ? So... What would be a good project team to propose for
inclusion ? The most important aspect is that the topic you're working on
must help further the OpenStack Mission, which is *to produce a ubiquitous
Open Source Cloud Computing platform that is easy to use, simple to implement,
interoperable between deployments, works well at all scales, and meets the
needs of users and operators of both public and private clouds*.

It is also very important that the team seamlessly merges into the OpenStack
Community. It must adhere to the
[4 Opens](https://governance.openstack.org/tc/reference/opens.html)
and follow the OpenStack
[principles](https://governance.openstack.org/tc/reference/principles.html).
The Technical Committee made a number of choices to avoid fragmenting the
community into several distinct silos. All projects use Gerrit to propose
changes, IRC to communicate, a set of
[approved programming languages](https://governance.openstack.org/tc/resolutions/20150901-programming-languages.html)...
Those rules are not set in stone, but we are unlikely to change them just
to facilitate the addition of one given new project team. All those
requirements are summarized in the
[new project requirements](https://governance.openstack.org/tc/reference/new-projects-requirements.html)
document.

The new team must also know its way around our various systems, development
tools and processes. Ideally the team would be formed from existing OpenStack
community members; if not the
[Project Team Guide](http://docs.openstack.org/project-team-guide/)
is there to help you getting up to speed.

### Where ?

OK, you're now ready to make the plunge. One question you may ask yourself
is whether you should contribute your project to an existing project team,
or ask to become a new official project team.

Since the recent
[project structure reform](https://governance.openstack.org/tc/resolutions/20141202-project-structure-reform-spec.html)
(a.k.a. the "big tent"), work in OpenStack is organized around groups of
people, rather than the general topic of your work. So you don't have to ask
the Neutron team to adopt your project just because it is about networking.
The real question is more... *is it the same team working on both
projects ?* Does the existing team feel like they can vouch for this new
work, and/or are willing to adapt their team scope to include it ? Having
two different groups under a single team and PTL only creates extra
governance problems. So if the teams working on it are distinct enough,
then the new project should probably be filed separately.

Another question you may ask yourself is whether alternate implementations
of the same functionality are OK. Is competition allowed between official
projects ? On one hand competition means dilution of effort, so you want
to minimize it. On the other you don't want to close evolutionary paths,
so you need to let alternate solutions grow. The Technical Committee answer
to that is: alternate solutions are allowed, as long as they are not
*gratuitously competing*. Competition must be between two different
technical approaches, not two different organizations or egos. Cooperation
must be considered first. This is all the more important the deeper you go
in the stack: it is obviously a lot easier to justify competition on an
OpenStack installer (which consumes all other projects), than on AuthN/AuthZ
(which all other projects rely on).

### How ?

Let's do this ! How to proceed ? The first and hardest part is to pick a
name. We want to avoid having to rename the project later due to trademark
infringement, once it has built some name recognition. A good rule of thumb
is that if the name sounds good, it's probably already used somewhere.
Obscure made-up names, or word combinations are less likely to be a registered
trademark than dictionary words (or person names). Online searches can help
weeding out the worst candidates. Please be good citizens and also avoid
collision with other open source project names, even if they are not
trademarked.

Step 2, you need to create the project on OpenStack infrastructure. See the
[Infra manual](http://docs.openstack.org/infra/manual/creators.html)
for instructions, and reach out on the #openstack-infra IRC channel if you
need help.

The final step is to propose a change to the
[openstack/governance](http://git.openstack.org/cgit/openstack/governance)
repository, to add your project team to the
[reference/projects.yaml](http://git.openstack.org/cgit/openstack/governance/tree/reference/projects.yaml)
file. That will serve as the official request to the Technical Committee,
so be sure to include a very informative commit message detailing how well
you fill the
[new projects requirements](https://governance.openstack.org/tc/reference/new-projects-requirements.html).
Good examples of that would be
[this change](https://review.openstack.org/#/c/402227/)
or [this one](https://review.openstack.org/#/c/353693/).

### When ?

The timing of the request is important. In order to be able to assess
whether the new team behaves like the rest of the OpenStack community,
the Technical Committee usually requires that the new team operates on
OpenStack infrastructure (and collaborates on IRC and the mailing-list)
for a few months.

We also tend to freeze new team applications during the second part of
the development cycles, as we start preparing for the release and the PTG.
So the optimal timing would be to set up your project on OpenStack
infrastructure around the middle of one cycle, and propose for official
inclusion at the start of the next cycle (before the first development
milestone). Release schedules are published
[here](https://releases.openstack.org/).

### That's it !

I hope this article will help you avoid the most obvious traps
in your way to become an official OpenStack project. Feel free to reach out
to me (or any other
[Technical Committee member](https://governance.openstack.org/tc/))
if you have questions or would like extra advice !


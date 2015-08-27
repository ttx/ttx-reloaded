Title: OpenStack Common Culture
Date: 2015-08-27 14:12
Author: Thierry Carrez
Tags: OpenStack
Slug: openstack-common-culture

We are 5 years into the OpenStack ride (and 3 years into the OpenStack
Foundation ride), and the challenges for our community are evolving.
In this article I want to talk about what I consider the most significant
threat for our open source community today: the loss of our common culture.

Over the past year we evolved the OpenStack project model to adopt an
[inclusive approach](http://ttx.re/the-way-forward.html). Project teams which
work on deliverables that help us achieve the OpenStack Mission, and which
follow our development and community practices should generally be accepted
under the "big tent". As we explained in
[this presentation in Vancouver](https://www.youtube.com/watch?v=TTe_bZtEKxo),
we moved from asking "is this OpenStack ?" to asking "are you OpenStack ?".

What does it mean to *be OpenStack* ? We wrote down a
[set of principles](http://governance.openstack.org/reference/new-projects-requirements.html),
based on the original [*four opens*](https://wiki.openstack.org/wiki/Open)
 that were defined at the very beginning of this journey. But
"being OpenStack" goes beyond that. It is to be aligned on a common goal,
be part of the same effort, be the same tribe. OpenStack relies on a number
of individuals working cross-project (on infrastructure, QA, documentation,
release processes, interoperability, user experience, API guidelines,
vulnerability management, election organization...). It is because we belong
to the same tribe that some people and organizations care enough about
"OpenStack" as a whole to dedicate time to those essential cross-project
efforts.

This is why we standardize on logged IRC channels as a communication medium,
why we ask that every project change goes through Gerrit, and why we should
very conservatively add new programming languages to the mix. Some people
advocate letting OpenStack project teams pick whatever language they want,
or letting them meet on that new trendy videoconferencing app, or letting
them track bugs on separate JIRA instances. More freedom sounds good at first
glance, but doing so would further fragment our community into specific silos
that all behave differently. Doing so would make recruiting for those
essential cross-project efforts even harder than it is today, while at the
same time making the work of those cross-project efforts significantly more
complex. Doing so would make our community crumble under its own weight.

We started this journey with a pretty strong common culture. It was mostly
oral tradition. We assumed that as OpenStack grew, our culture would
naturally be assimilated by new members. And it did, for quite some time.
But today we are at a point where we dramatically expanded our community
(we doubled the number of project teams over the last year) and our common
culture did not naturally transmit to newcomers. Silos with local traditions
have formed. Teams don't all behave in the same way anymore. Most team
members only care about a single project team. We struggle to move from one
project to another. We struggle to provide common solutions that work for
everyone. We struggle to recruit for cross-project efforts more than we ever
did. OpenStack's future as a community is at risk. It's time to hold the
culture line, rather than time to further relax it.

It is also more than time that we document our common culture, so that it
can be explicitly communicated to everyone in the OpenStack ecosystem
(current and prospective members). We started a workgroup at the
[Technical Committee](http://governance.openstack.org/), held a
[virtual sprint](https://wiki.openstack.org/wiki/VirtualSprints) to get a
base version written, and now here it is: the first version of the
[OpenStack Project team guide](http://docs.openstack.org/project-team-guide).
Read it, refer to it, communicate it to your OpenStack community fellows,
propose changes to it. It is an essential tool for us to overcome this new
challenge. It's certainly not the only tool, and I hope we'll be able to
dedicate a cross-project session at the Mitaka Design Summit in Tokyo to
further discuss this topic.

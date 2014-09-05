Title: An history of OpenStack project governance
Date: 2013-06-20 10:18
Author: Thierry Carrez
Tags: OpenStack, Popular
Slug: history-of-openstack-governance

Over the last 3 years, the technical governance of the OpenStack open
source project evolved a lot, and most recently [last
Tuesday](https://lists.launchpad.net/openstack/msg24526.html). As an
elected member of that governance body since April 2011, I witnessed
that evolution from within and helped in drafting the various models
over time. Now seems like a good time to look back in history, and clear
a few misconceptions about the OpenStack project governance along the
way.

### The POC

The project was originally created by Rackspace in July 2010 and seeded
with code from NASA (Nova) and Rackspace (Swift). At that point an
[initial project
governance](https://wiki.openstack.org/w/index.php?title=Governance&oldid=8370)
was set up. There was an *Advisory Board* (which was never really
created), the *OpenStack Architecture Board*, and technical committees
for each subproject, each lead by a Technical Lead. The OpenStack
Architecture Board had 5 members appointed by Rackspace and 4 elected by
the community, with 1-year to 3-year (!) terms. The technical leads for
the subprojects were appointed by Rackspace.

By the end of the year 2010 the Architecture Board was renamed *Project
Oversight Committee* (POC), but its structure [didn't
change](https://wiki.openstack.org/w/index.php?title=Governance&oldid=8377).
While it left room for community input, the POC was rightfully seen as
fully controlled by Rackspace, which was a blocker to deeper involvement
for a lot of the big players in the industry.

It was a danger for the open source project as well, as the number of
contributors external to Rackspace grew. As countless examples prove,
when the leadership of an open source project is not seen as
representative of its contributors, you face the risk of a revolt, a
fork of the code and seeing your contributors leave for a more
meritocratic and representative alternative.

### The PPB

In March 2011, a significant change was
[introduced](http://www.openstack.org/blog/2011/03/openstack-governance-update/)
to address this perceived risk. Technical leads for the 3 projects
(Nova, Swift, and Glance at that point) would from now on be directly
elected by their contributors and called *Project Technical Leads*
(PTLs). The POC was replaced by the *Project Policy Board* (PPB), which
had 4 seats appointed by Rackspace, 3 seats for the above PTLs, and 5
seats directly-elected by all the contributors of the project. By spring
2012 we grew to 6 projects and therefore the PPB had 15 members.

This was definitely an improvement, but it was not perfect. Most
importantly, the governance model itself was still owned by Rackspace,
which could potentially change it and displace the PPB if it was ever
unhappy with it. This concern was still preventing OpenStack from
reaching the next adoption step. In October 2011, Rackspace therefore
[announced](http://www.openstack.org/blog/2011/10/openstack-foundation/)
that they would set up an independent Foundation. By the summer of 2012
that move was completed and Rackspace had transfered the control over
the governance of the OpenStack project to the [OpenStack
Foundation](http://www.openstack.org/foundation/).

### The TC

At that point the governance was split into two bodies. The first one is
the *Board of Directors* for the Foundation itself, which is responsible
for promoting OpenStack, protecting its trademark, and deciding where to
best spend the Foundation's sponsors money to empower future development
of OpenStack.

The second body was the successor to the PPB, the entity that would
govern the open source project itself. A critical piece in the
transition was the need to preserve and improve the independence of the
technical meritocracy. The bylaws of the Foundation therefore instituted
the *Technical Committee*, a successor for the PPB that would be
self-governed, and would no longer have appointed members (or any
pay-to-play members). The Technical Committee would be [completely
elected](https://wiki.openstack.org/w/index.php?title=Governance/Foundation/TechnicalCommittee&oldid=3208)
by the active technical contributors: a seat for each elected PTL, plus
5 directly-elected seats.

### TC 2.0

The TC started out in September 2012 as an 11-member committee, but with
the addition of 3 new projects (and the creation of a special seat for
Oslo), it grew to 15 members in April 2013, with the perspective to grow
to 18 members in Fall 2013 if all projects applying for incubation
recently get finally accepted. With the introduction of the
["integrated" project
concept](https://lists.launchpad.net/openstack/msg20881.html) (separate
from the "core" project concept), we faced the addition of even more
projects in the future and committee bloat would inevitably ensue. That
created a potential for resistance to the addition of "small" projects
or the splitting of existing projects (which make sense technically but
should not be worth adding yet another TC seat).

Another issue was the ever-increasing representation of "vertical"
functions (project-specific PTLs elected by each project contributors)
vs. general people elected by all contributors. In the original PPB mix,
there were 3 "vertical" seats for 5 general seats, which was a nice mix
to get specific expertise but overall having a cross-project view. With
the growth in the number of projects, in the current TC we had 10
"vertical" seats for 5 general seats. Time was ripe for a reboot.

[Various models](https://wiki.openstack.org/wiki/TC_Membership_Models)
were considered and discussed, and while everyone agreed on the need to
change, no model was unanimously seen as perfect. In the end, simplicity
won and we picked a model with [13 directly-elected
members](https://wiki.openstack.org/w/index.php?title=Governance/Foundation/TechnicalCommittee&oldid=24429),
which will be put in place at the Fall 2013 elections.

### Power to the active contributors

This new model is a direct, representative model, where if you recently
authored a change for an OpenStack project, you get one vote, and a
chance every 6 months to choose new people to represent you. This model
is pretty flexible and should allow for further growth of the project.

Few open source projects use such a direct governance model. In Apache
projects for example (often cited as a model of openness and
meritocracy), the oversight committee equivalent to OpenStack's TC would
be the PMC. In [most](http://cloudstack.apache.org/bylaws.html) cases,
PMC membership is self-sustaining: existing PMC members ultimately
decide, through discussions and
[votes](http://www.apache.org/dev/pmc.html#newpmc) on the private PMC
list, who the new PMC members should be. In contrast, in OpenStack the
recently-active contributors end up being in direct control of who their
leaders are, and can replace the Technical Committee members if they
feel like they are not relevant or representing them anymore. Oh, and
the TC doesn't use a private list: all our meetings are
[public](http://eavesdrop.openstack.org/meetings/tc/) and our
discussions are
[archived](http://lists.openstack.org/pipermail/openstack-tc/).

As far as open source projects governance models go, this is as open,
meritocratic, transparent and direct as it gets.

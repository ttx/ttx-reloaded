Title: Splitting out the OpenStack Design Summit
Date: 2016-02-22 16:22
Author: Thierry Carrez
Tags: OpenStack
Slug: splitting-out-design-summit


In a global and virtual community, high-bandwidth face-to-face time is
essential. This is why we made the OpenStack Design Summits an integral
part of our processes from day 0. Those were set at the beginning of each
of our development cycles to help set goals and organize the work for the
upcoming 6 months. At the same time and in the same location, a more
traditional conference was happening, ensuring a lot of interaction between
the upstream (producers) and downstream (consumers) parts of our community.

This setup, however, has a number of issues. For developers first: the
"conference" part of the common event got bigger and bigger and it is
difficult to focus on upstream work (and socially bond with your teammates)
with so much other commitments and distractions. The result is that our
design summits are a lot less productive than they used to be, and we
organize other events ("midcycles") to fill our focus and small-group
socialization needs. The timing of the event (a couple of weeks after the
previous cycle release) is also suboptimal: it is way too late to gather any
sort of requirements and priorities for the already-started new cycle, and
also too late to do any sort of work planning (the cycle work started almost
2 months ago).

But it's not just suboptimal for developers. For contributing companies,
flying all their developers to expensive cities and conference hotels so
that they can attend the Design Summit is pretty costly, and the goals of
the summit location (reaching out to users everywhere) do not necessarily
align with the goals of the Design Summit location (minimize and balance
travel costs for existing contributors). For the companies that build products
and distributions on top of the recent release, the timing of the common event
is not so great either: it is difficult to show off products based on the
recent release only two weeks after it's out. The summit date is also too
early to leverage all the users attending the summit to gather feedback on
the recent release -- not a lot of people would have tried upgrades by
summit time. Finally a common event is also suboptimal for the events
organization : finding venues that can accommodate both events is becoming
increasingly complicated.

Time is ripe for a change. After Tokyo, we at the Foundation have been
considering options on how to evolve our events to solve those issues. This
proposal is the result of this work. There is no perfect solution here (and
this is still work in progress), but we are confident that this strawman
solution solves a lot more problems than it creates, and balances the needs
of the various constituents of our community.

The idea would be to split the events. The first event would be for upstream
technical contributors to OpenStack. It would be held in a simpler, scaled-back
setting that would let all OpenStack project teams meet in separate rooms,
but in a co-located event that would make it easy to have ad-hoc cross-project
discussions. It would happen closer to the centers of mass of contributors,
in less-expensive locations.

More importantly, it would be set to happen a couple of weeks **before** the
previous cycle release. There is a lot of overlap between cycles. Work on a
cycle starts at the previous cycle feature freeze, while there is still 5
weeks to go. Most people switch full-time to the next cycle by RC1.
Organizing the event just after that time lets us organize the work and
kickstart the new cycle at the best moment. It also allows us to use our time
together to quickly address last-minute release-critical issues if such
issues arise.

The second event would be the main downstream business conference, with
high-end keynotes, marketplace and breakout sessions. It would be organized
two or three months **after** the release, to give time for all downstream
users to deploy and build products on top of the release. It would be the best
time to gather feedback on the recent release, and also the best time to have
strategic discussions: start gathering requirements for the next cycle,
leveraging the very large cross-section of all our community that attends
the event.

To that effect, we'd still hold a number of strategic planning sessions at
the main event to gather feedback, determine requirements and define overall
cross-project themes, but the session format would not require all project
contributors to attend. A subset of contributors who would like to participate
in these sessions can collect and relay feedback to other team members for
implementation (similar to the Ops midcycle). Other contributors will also
want to get more involved in the conference, whether that's giving
presentations or hearing user stories.

The split should ideally reduce the needs to organize separate in-person
mid-cycle events. If some are still needed, the main conference venue and
time could easily be used to provide space for such midcycle events (given
that it would end up happening in the middle of the cycle).

In practice, the split means that we need to stagger the events and cycles.
We have a long time between Barcelona and the Q1 Summit in the US, so the
idea would be to use that long period to insert a smaller cycle (Ocata) with
a release early March, 2017 and have the first specific contributors event
at the start of the P cycle, mid-February, 2017. With the already-planned
events in 2016 and 2017 it is the earliest we can make the transition. We'd
have a last, scaled-down design summit in Barcelona to plan the shorter cycle.

![cycle_overlap]({filename}/images/overlap2.png)

With that setup, we hope that we can restore the productivity and focus of
the face-to-face contributors gathering, reduce the need to have midcycle
events for social bonding and team building, keep the cost of getting all
contributors together once per cycle under control, maintain the feedback
loops with all the constituents of the OpenStack community at the main event,
and better align the timing of each event with the reality of the release
cycles.

NB: You will note that I did not name the separated event "Design Summit" --
that is because *Design* will now be split into feedback/requirements
gathering (the **why** at the main event) and execution planning and
kickstarting (the **how** at the contributors-oriented event), so that name
doesn't feel right anymore. We can bikeshed on the name for the new event
later :)

This was also posted to the [openstack-dev ML](http://lists.openstack.org/pipermail/openstack-dev/2016-February/087161.html):
please comment and follow-up there if you have thoughts to share.

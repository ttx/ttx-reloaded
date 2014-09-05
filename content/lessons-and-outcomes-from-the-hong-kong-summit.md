Title: Lessons and outcomes from the Hong-Kong summit
Date: 2013-11-13 14:23
Author: Thierry Carrez
Tags: OpenStack
Slug: lessons-and-outcomes-from-the-hong-kong-summit

Just back from an amazing week at the OpenStack Summit in Hong-Kong, I
would like to share a number of discussions we had (mainly on the
[release management
track](http://icehousedesignsummit.sched.org/overview/type/release+management))
and mention a few things I learned there.

First of all, **Hong-Kong is a unique city**. Skyscrapers built on
vertiginous slopes, crazy population density, awesome restaurants, shops
everywhere... Everything is clean and convenient (think: Octopus cards),
even as it grows extremely fast. Everyone should go there at least one
time in their lives !

On the Icehouse Design Summit side,**the collaboration magic happened
again**. I should be used to it by now, but it is still amazing to build
this level playing field for open design, fill it with smart people and
see them make so much progress over 4 days. We can still improve,
though: for example I'll make sure we get whiteboards in every room for
the next time :). As was mentioned in the feedback session, we are
considering staggering the design summit and the conference (to let
technical people participate to the latter), set time aside to discuss
cross-project issues, and set up per-project space so that collaboration
can continue even if there is no scheduled "session" going on.

I have been mostly involved in [release management
sessions](https://wiki.openstack.org/wiki/Summit/Icehouse/Etherpads#Release_Management).
We discussed the [Icehouse release
schedule](https://wiki.openstack.org/wiki/Icehouse_Release_Schedule),
with a **proposed release date of April 17**, and the possibility to
have a pre-designated **"off" week** between release and the J design
summit. We discussed changes in the format of the weekly
[project/release status
meeting](https://wiki.openstack.org/wiki/Meetings/ProjectMeeting), where
we should move per-project status updates off-meeting to be able to
focus on cross-project issues instead. During this cycle we should also
work on streamlining library release announcements. For stable branch
maintenance, we decided to officially drop support for version n-2 by
feature freeze (rather than at release time), which reflects more
accurately what ended up being done during the past cycles. The security
support is now aligned to stable branch support, which should make sure
the vulnerability management team (VMT) doesn't end up having to
maintain old stable branches that are already abandoned by the stable
branch maintainers. Finally, the VMT should review the projects from all
official programs to come up with a clear list of what projects are
actually security-supported and which aren't.

Apart from the release management program, I'm involved in two pet
projects: [Rootwrap](https://wiki.openstack.org/wiki/Rootwrap) and
[StoryBoard](https://github.com/openstack-infra/storyboard).
**Rootwrap** should be split from the oslo-incubator into its own
package early in the Icehouse cycle, and its usage in Nova, Cinder and
Neutron should be reviewed to result in incremental strengthening.
**StoryBoard** (our next-generation task tracker) generated a lot of
interest at the summit, I expect a lot of progress will be made in the
near future. Its architecture might be overhauled from the current POC,
so stay tuned.

Finally, it was great meeting everyone again. Our PTLs and Technical
Committee members are a bunch of awesome folks, this open source project
is in great hands. More generally, it seems that we not only designed a
new way of building software, we also created a network of individuals
and companies interested in that kind of open collaboration. That
network explains why it is so easy for people to jump from one company
to another, while continuing to do the exact same work for the OpenStack
project itself. And for developers, I think it's a great place to be in:
if you haven't already, you should definitely consider joining us.

 

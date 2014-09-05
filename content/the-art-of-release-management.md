Title: The art of release management
Date: 2010-11-08 21:37
Author: Thierry Carrez
Tags: Management, OpenStack
Slug: the-art-of-release-management

Last week I started a new job, working for Rackspace Hosting as the
Release Manager for the Openstack project. I'm still very much working
from home on open source software, so that part doesn't change. However,
there are some subtle differences.

First of all, Openstack is what we call an upstream project. Most of my
open source work so far involves *distribution work*: packaging and
delivering various open source software components into a
well-integrated, tested and security-maintained distribution. This is
hard work, one that is never completely finished or perfect. It is also
a necessary part of the open source ecosystem: without distributions,
most software would not be easily available for use.

*Upstream work*, on the other hand, is about developing the software in
the first place. It's a more creative work, in a much more controlled
environment. The Openstack project is the new kid on the block of cloud
computing software, one that strives to become the open source standard
for building cloud infrastructures everywhere. It was announced in July,
so it's relatively young. There are lots of procedures and processes to
put in place, an already-large developer group, and an ever-growing
community of users and partners. The software itself is positioned to
run in high-demand environments: The storage component is in production
use at Rackspace, the compute component is in production use at NASA.
Openstack is planned to fully replace the current Rackspace Cloud
software next year, and a number of governments plan to use it to power
their local cloud infrastructure. Those are exciting times.

What does an open source project Release Manager do ? Well first, as it
says on the tin, it manages the release process. Every 3 or 6 months,
Openstack will release a new version of its components, and someone has
to make sure that that happens. That's OK, but what do I do the other 50
weeks of the year ? Well, release managers also manage the release
**cycle**. A cycle goes through four stages: Design, Development, QA and
Release. It is the job of the release manager to drive and help the
developer community through those stages, follow work in progress,
making sure everyone knows about the steps and freezes, and granting
exceptions when necessary. At the very end, he must balance between the
importance of a bug and the risk of regression the bugfix introduces:
it's better to release with a known bug than with an unknown regression.
He is ultimately responsible for the delivery, on time, of the complete
release cycle. And yes, if you condense everything to 3 or 6 months,
this is a full-time job :)

My duties also include ensuring that the developers have everything they
need to work at their full potential and that the project is
transparent. I also have to make sure the developer community is a
welcoming environment for prospective new contributors, and present the
project as a technical envangelist in conferences. And if I still have
free time, I may even write some code where I need to scratch an itch.
All in all, it's a pretty exciting job, and I'm very happy to meet
everyone this week at the Openstack design summit in ~~Orlando~~ San
Antonio.

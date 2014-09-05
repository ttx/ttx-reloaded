Title: Grizzly, the day after
Date: 2013-04-05 13:08
Author: Thierry Carrez
Tags: OpenStack
Slug: grizzly-the-day-after

The OpenStack Grizzly release of yesterday officially closes the Grizzly
development cycle. But while I try to celebrate and relax, I can't help
from feeling worried and depressed on the hours following the release,
as we discover bugs that we could have (should have ?) caught before
release. It's a kind of postpartum depression for release managers;
please consider this post as part of my therapy.

### Good

We'd naturally like to release when the software is "ready", "good", or
"bug-free". Reality is, with software of the complexity of OpenStack,
onto which we constantly add new features, there will always be bugs.
So, rather than releasing when the software is bug-free, we "release"
when waiting more would not really change the quality of the result. We
release when it's time.

In OpenStack, we invest a lot in automated testing, and each proposed
commit goes through an extensive set of unit and integration tests. But
with so many combinations of deployment options, there are still dark
corners that will only be explored by users as they apply the new code
to their specific use case. We encourage users to try new code *before*
release, by publishing and making noise about milestones, release
candidates... But there will always be a significant number of users who
will not try new code until the point in time we call "release". So
there will always be significant bugs that are discovered (and fixed)
after release day.

### The best point in time

What we need to do is pick the right moment to "release": when all known
release-critical issues are fixed. When the benefits of waiting more are
not worth the drawbacks of distracting developers from working on the
next development cycle, or of abandoning the benefits of a predictable
time-based common release.

That's the role of the [Release
Candidates](https://wiki.openstack.org/wiki/Release_Cycle) that we
produce in the weeks before the release day. When we fixed all known
release-critical bugs, we create an RC. If we find new ones before the
release day, we fix them and regenerate a new release candidate. On
release day, we consider the current release candidates as "final" and
publish them.

The trick, then, is to pick the right length for this feature-frozen
period leading to release, one that gives enough time for each of the
projects in OpenStack to reach this the first release candidate
(meaning, "all known release-critical bugs fixed"), and publish this RC1
to early testers. For Grizzly, it looked like this:

![grizzly RCs]({filename}/images/grizzly-rcs.png)

This graph shows the number of release-critical bugs in various projects
over time. We can see that the length of the pre-release period is about
right: waiting more would not have resulted in a lot more bugs to be
fixed. We basically needed to release to get more users to test and
report the next bugs.

### The Grizzly is still alive

The other thing we need to have is a process to continue to fix bugs
after the "release". We document the most obvious regressions in the
constantly-updated [Release
Notes](https://wiki.openstack.org/wiki/ReleaseNotes/Grizzly). And we
handle the Grizzly bugs using the stable release update process.

After release, we maintain a branch where important bugfixes are
backported and from which we'll publish point releases. This
**stable/grizzly** branch is maintained by the OpenStack stable
maintenance team. If you see a bugfix that should definitely be
backported, you can tag the corresponding bug in Launchpad with the
*grizzly-backport-potential* tag to bring it to the team's attention.
For more information on the stable branches, I invite you to read this
[wiki page](https://wiki.openstack.org/wiki/StableBranch).

### Being pumped up again

The post-release depression usually lasts a few days, until I realize
that not so many bugs were reported. The quality of the new release is
actually always an order of magnitude better than the previous releases,
due to 6-month worth of improvements in our amazing continuous
integration system ! We actually did an incredible job, and it will only
get better !

The final stage of recovery is when our fantastic community gets all
together at the OpenStack Summit. 4 days to witness and celebrate our
success. 4 days to recharge the motivation batteries, brainstorm and
discuss what we'll do over the next 6 months. We are living awesome
times. See you there.

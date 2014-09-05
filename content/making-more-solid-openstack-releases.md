Title: Making more solid OpenStack releases
Date: 2012-01-18 14:16
Author: Thierry Carrez
Tags: OpenStack
Slug: making-more-solid-openstack-releases

As we pass the middle of the [Essex development
cycle](http://wiki.openstack.org/EssexReleaseSchedule), questions about
the solidity of this release start to pop up. After all, the previous
releases were far from stellar, and with more people betting their
business on OpenStack we can't really afford another half-baked release.

Common thinking (mostly coming from years of traditional software
development experience) is that we shouldn't release until it's ready,
or good enough, and calls early for pushing back the release dates. This
assumes the issue is incidental: that we underestimated the time it
would take our finite team of internal developers working on bugs to
reach a sufficient level of quality.

OpenStack, being an open source project produced by a large community,
works differently. We have a near-infinite supply of developers. The
issue is, unfortunately, more structural than incidental. The lack of
solidity for a release comes from:

-   **Lack of focus on generic bugfixes.** Developers should work on
    fixing bugs. Not just the ones they filed or the ones blocking them
    in their feature-adding frenzy. Fixing identified, targeted, known
    issues. The bugtracker is full of them, but they don't get
    attention.
-   **Not enough automated testing to efficiently catch regressions.**
    Even if everyone was working on bug fixes, if half your fixes end up
    creating a set of regressions, then there is no end to it.
-   **Lack of bug triaging resources.** Only a few people work on
    confirming, triaging and prioritizing the flow of incoming bugs. So
    the bugs that need the most attention are lost in the noise.

For the Diablo cycle, we had less than a handful of people focused on
generic bugfixing. The rest of our 150+ authors were busy working on
something else. Pushing back the release for a week, a month or a year
won't help OpenStack solidity if the focus doesn't switch. And if our
focus switches, then there will be no need for a costly release delay.

#### Acting now to make Essex a success

During the Essex cycle, our Project Technical Leads have done their
share of the work by using a very early milestone for their feature
freeze. Keystone, Glance and Nova will freeze at *Essex-3*, giving us 10
weeks for bugfixing work (compared to the 4 weeks we had for Diablo).
Now we need to take advantage of that long period and really switch our
mindset away from feature development and towards generic bug fixing.

Next week we'll hit feature freeze, so **now** is the time to switch. 
If we could:

-   have some more developers working on increasing our integration and
    unit test coverage
-   have the rest of the developers really working on generic bug fixing
-   have very active core reviewers that get more anal-retentive as we
    get closer to release, to avoid introducing regressions that would
    not be caught by our automated tests

...then I bet that it will lead to a stronger release than any delaying
of the release could give you. Note that we'll also have a [bug
squashing day](http://wiki.openstack.org/BugSquashingDay/20120202) on
February 2 that will hopefully help us getting on top of old, deprecated
and easy fixes, and give us a clear set of targets for the rest of the
cycle.

That's on our ability to switch our focus that hinges the quality of
future OpenStack releases. That's on what we'll be judged. The world
awaits, and the time is now.

Title: Time-based releases are good for community
Date: 2011-07-01 10:11
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: time-based-good-for-community

There was a bit of
[discussion](http://tlohg.com/distributions-projects-and-releases)
lately on feature-based vs. time-based release schedules in OpenStack,
and here are my thoughts on it. In a feature-based release cycle, you
release when a given set of features is implemented, while in a
time-based release cycle, you release at a predetermined date, with
whatever is ready at the time.

### Release early, release often

One the basic principles in open source (and agile) is to release early
and release often. This allows fast iterations, which avoid the classic
drawbacks of [waterfall
development](http://en.wikipedia.org/wiki/Waterfall_model). If you push
that logic to the extreme, you can release at every commit: that is what
continuous deployment is about. Continuous deployment is great for web
services, where there is only one deployment of the software and it runs
the latest version.

OpenStack projects actually provide builds (and packages) for every
commit made to development trunk, but we don't call them releases. For
software that has multiple deployers, having "releases" that combine a
reasonable amount of new features and bugfixes is more appropriate.
Hence the temptation of doing feature-based releases: release often,
whenever the next significant feature is ready.

### Frequent feature-based releases

The main argument of supporters of frequent feature-based releases is
that time-based cycles are too long, so they delay the time it takes for
a given feature to be available to the public. But time-based isn't
about "a long time". It's about "a predetermined amount of time". You
can make that "predetermined amount of time" as small as needed...

Supporters of feature-based releases say that time-based releases are
good for distributions, since those have limited bearing on the release
cycles of their individual subcomponents. I'd argue that time-based
releases are always better, for anyone that wants to do open development
in a community.

### Time-based releases as a community enabler

If you work with a developer community rather than with a single-company
development group, the project doesn't have full control over its
developers, but just limited influence. Doing feature-based releases is
therefore risky, since you have no idea how long it will take to have a
given feature implemented. It's better to have frequent time-based
releases (or milestones), that regularly delivers to a wider audience
what happens to be implemented at a given, predetermined date.

If you work with an open source community rather than with a
single-company product team, you want to help the different separate
stakeholders to synchronize. Pre-announced release dates allow everyone
(developers, testers, distributions, users, marketers, press...) to be
on the same line, following the same cadence, responding to the same
rhythm. It might be convenient for developers to release "whenever it
makes sense", but the wider community benefits from having predictable
release dates.

It's no wonder that most large open source development communities
switched from feature-based releases to time-based releases: it's about
the only way to "release early, release often" with a large community.
And since we want the OpenStack community to be as open and as large as
possible, we should definitely continue to do time-based releases, and
to announce the schedule as early as we can.

 

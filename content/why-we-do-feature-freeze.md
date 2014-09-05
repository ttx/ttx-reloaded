Title: Why we do Feature freeze
Date: 2014-03-06 09:15
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: why-we-do-feature-freeze

Yesterday we entered the [Icehouse development
cycle](https://wiki.openstack.org/wiki/Icehouse_Release_Schedule)
Feature Freeze. But with the incredible growth of the OpenStack
development community (508 different contributors over the last 30 days,
including 101 new ones !), I hear a lot of questions about it. I've
explained it on various forums in the past, but I figured it couldn't
hurt to write something a bit more definitive about it.

## Why

Those are valid questions. Why freeze features ? That sounds very
anti-agile. Isn't our test-centric development model supposed to protect
us from regressions anyway ? Let's start with what feature freeze is
not. Feature freeze should only affect the integrated OpenStack release.
If you don't release (i.e. if you don't special-case certain moments in
the development), then feature freezing makes little sense. It's also
not a way to punish people who failed to meet a deadline. There are
multiple reasons that a given feature will miss a deadline, and most of
those are not the fault of the original author of the feature. We do
time-based releases, so some features and some developers will
necessarily be caught on the wrong side of the fence at some point and
need to wait for the next boat. It's an artifact of open innovation
projects.

Feature freeze (also known as "FF") is, obviously, about stopping adding
new features. You may think of it as artificially blocking your
progress, but this has a different effect on other people:

-   As was evidenced by the Icehouse cycle, good **code reviewers** are
    a scarce resource. The first effect of feature freeze is that it
    limits the quantity of code reviews and make them all about
    bugfixes. This lets reviewers concentrate on getting as many
    bugfixes in as possible before the "release". It also helps
    **developers** spend time on bugfixes. As long as they can work on
    features, their natural inclination (or their employer orders) might
    conflict with the project interest at this time in the cycle, which
    is to make that point in time we call the "release" as bug-free as
    possible.

-   From a **QA** perspective, stopping the addition of features means
    you can spend useful time testing "in real life" how OpenStack
    behaves. There is only so much our automated testing will catch. And
    it's highly frustrating to spend time testing software that
    constantly changes under you.

-   QA is not the only group that needs to catch up. For the
    **documentation** team, the **I18N** team, feature freeze is
    essential. It's difficult to write documentation if you don't know
    what will be in the end product. It's frustrating to translate
    strings that are removed or changed the next day.

-   And then you have all the downstream consumers of the release that
    can use time to prepare it. **Packagers** need software that doesn't
    constantly change and add dependencies, so that they can prepare
    packages for OpenStack projects that are released as close to our
    release date as possible. The **marketing team** needs time to look
    into what was produced over the cycle and arrange it in key messages
    to communicate to the outside world at release time.

-   Finally, for **release management**, feature freeze is a tool to
    reduce risk. The end goal is to avoid introducing an embarassing
    regression just before release. By gradually limiting the impact of
    what we accept in the release branch (using feature freeze, but also
    using the [RC
    dance](https://wiki.openstack.org/wiki/ReleaseCycle#Pre-release_.28Release_Candidates_dance.29)
    that comes next), we try our best to prevent that.

## Exceptions

For all these groups, it's critical that we stop adding features,
changing behavior, adding new configuration options, or changing
translatable strings as early as possible. Of course, it's a trade-off.
There might be things that are essential to the success of the release,
or things that are obviously risk-limited. That's why we have an
exception process: the Feature Freeze exceptions ("FFEs").

Feature freeze exceptions may be granted by the PTL (with the friendly
but strong advice from the release management team). The idea is to
weigh the raw benefit of having that feature **in** the release, against
the complexity of the code that is being brought in, its risk of causing
a regression, and how deep we are in feature freeze already. A
self-contained change that is ready to merge a few days after feature
freeze is a lot more likely to get an exception than a refactoring of a
key layer that still needs some significant work to land. It also
depends on how many exceptions were already granted on that project,
because at some point adding anything more just causes too much
disruption.

It's a difficult call to make, and the release management team is here
to help the PTLs make it. If your feature gets denied, don't take it
personally. As you saw there are a large number of factors involved. Our
common goal is to raise the quality of the end release, and *every*
feature freeze exception we grant is a step *away* from that. We just
can't take that many steps back and still guaranteeing we'll win the
race.

 

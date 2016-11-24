Title: OpenStack TC mythbusting
Date: 2016-11-28 10:38
Author: Thierry Carrez
Tags: OpenStack
Slug: openstack-tc-mythbusting

On several occasions over the last months, I heard people exposing *truths*
about the OpenStack Technical Committee. However, those positions were often
inaccurate or incomplete. Arguably we are not communicating enough: governance
changes and resolutions that are brought to the TC are just approved or
rejected. That binary answer is generally not the whole story, and with only
the headline, it is easy to read too much in a past decision. We should do a
better job at communicating beyond that simple answer when the topic is more
complex, and at continuously explaining the role and limits of the TC.
Hopefully this blogpost will help, by busting some of those myths.

### Myth #1: "the TC doesn't want Go in OpenStack"

This one comes from the recent rejection of a resolution proposing to add
golang to the list of approved languages, to support merging the *hummingbird*
feature branch into Swift's *master* branch. A more accurate way to present
that decision would be to say that a (short) majority of the TC members was not
supporting the addition of golang at that time and under the proposed
conditions. In summary it was more of a "not now, not this way" than a "never".

There were a number of reasons for this decision, but the crux was: adding a
language creates fragmentation and a support cost for all of the OpenStack
community, so we need to make sure "OpenStack" as a whole is successful with
it, beyond any specific project. That means for example having a clear plan
for integrating Go within all our standing processes, while trying to prevent
duplication of effort or gratuitous rewrites. The discussion was actually
recently restarted by Flavio in
[this change](https://review.openstack.org/#/c/398875/). We'll need
resources to make this a success, so if you care, please jump in to help.

### Myth #2: "the TC doesn't like competition with existing projects"

I'm not exactly sure where this one comes from. I can't think of any specific
TC decision that would explain it. Historically, back when we had *programs*,
a given team would own a given problem space and could essentially lock
alternatives out. But the *Big Tent* project structure reform changed that,
allowing competition to happen within our community.

Yes, we still want to encourage cooperation wherever it's possible, so we
still have a requirement which says "*where it makes sense, the project
cooperates with existing projects rather than gratuitously competing or
reinventing the wheel*". But as long as the new project is different or
presents a different value proposal, it should be fair game. For example we
accepted the Monasca team in the same problem space as the Telemetry team.
And we have several teams working on various deployment recipes.

That said, having competitive solutions in OpenStack on key problem spaces
(like base compute or networking services) creates interesting second-order
questions in terms of what is "core", trademark usage and interoperability.
Those are arguably more downstream concerns than upstream concerns, but that
explains why the deeper you go, the more difficult the community discussion
is likely to be.

### Myth #3: "the TC does not set any direction"

There are multiple variants on that one, from "OpenStack needs a benevolent
dictator" to "a camel is a horse designed by a committee". The idea behind it
is that the TC needs to have a very opinionated plan for OpenStack and somehow
force everyone in our community to follow it. Part of this myth is trying to
apply single-vendor software development theory to an open collaboration, and
misunderstanding how other large open source projects (like the Linux kernel)
work.

While the TC members are all well-respected in our community, we can't
unilaterally decide everything for 2500+ developers from 300+ different
organizations, and expect them all to execute The Plan. What the TC can do,
however, is to define the mission, provide an environment, set principles,
enforce common practices, and arbitrate conflicts. In painting terms, the TC
provides the frame, the subject of the painting, a color palette and the
techniques that can be used. But it doesn't paint. Painting is done at each
project team level.

In this cycle, the TC started to drive some simple cross-community goals. The
idea is to collectively make visible progress on a given topic over the course
of a release cycle, to pay back technical debt or to implement a simple feature
across all of OpenStack projects. But this is done as a goal the community
agrees to work on, rather than a top-down mandate.


### Myth #4: "the TC, due to the Big Tent, prevents proper focus"

This one is interesting, and I think its roots lie in some misunderstanding of
open source community dynamics. If you consider a finite set of resources and
a zero-sum-game community, then of course adding more projects results in less
resources being dedicated to "important projects". But an open community like
OpenStack is not a finite set of resources. The people and the organizations
in the OpenStack community work and cooperate on a number of projects. Before
the big tent, some of those would not be considered part of the OpenStack
projects, despite helping with the OpenStack mission and following the
OpenStack development principles, and therefore essentially being developed
by the OpenStack community. 

Considering more (or less) projects as being part of our community doesn't
decrease (or increase) focus on "important projects". It's up to each
organization in OpenStack to focus on the set of projects it considers
important. For more on that, go read Ed Leafe's
[brilliant blogpost](https://blog.leafe.com/openstack-focus/), he expressed
it better than I can. Of course there are some efforts (like packaging)
where adding more projects results in diluting focus. But with every added
project comes new blood in our community (rather than artificially keeping it
out), and some of that new blood ends up helping on those efforts. It's not
a zero-sum game, and the big tent makes sure we are open to new ways of
achieving the OpenStack mission and have an inclusive and welcoming community.


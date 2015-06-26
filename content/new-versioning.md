Title: New OpenStack component versioning
Date: 2015-06-26 14:45
Author: Thierry Carrez
Tags: OpenStack
Slug: new-versioning


Yesterday we reached the liberty-1 development milestone. You may have noticed
from the [announcement](http://lists.openstack.org/pipermail/openstack-announce/2015-June/000391.html)
that the various components released were all using new, different version
numbers. What's going on here ?

## Once upon a time

Since the beginning of OpenStack we've been using two versioning schemes.
One was for projects released once every 6 months and following a schedule
of development milestones and release candidates. Those would be using
a YEAR.N version number (like 2015.1 for Kilo).

Another was used by Swift, which was already mature when OpenStack started,
and which released intermediary versions as-needed throughout the cycle. It
would use a X.Y.Z version number which looked a lot more like semantic
versioning.

At the end of the cycle, we would coordinate a final release that would
combine both. For example the "Kilo" release would be made of Nova 2015.1.0,
Swift 2.3.0, and everything else at 2015.1.0.

## Recent developments

A few things happened over the last two cycles. First, we released more and
more libraries, and those would follow a strict X.Y.Z semantic versioning.
Those would also have an final release in the cycle, from which a stable
branch would be maintained for critical bugfixes and vulnerability fixes. So
the portion of commonly-versioned YEAR.N deliverables was fast decreasing.

Second, some projects got more mature and/or more able to release
fully-functional intermediary releases as-needed. As a community, we still
can't support more than one stable branch every 6 months, so those intermediary
releases won't get backports, but past a given maturity step, it's still a
great thing to push new features to bleeding-edge users as early and often as
we can. For those a YEAR.N synchronized versioning scheme would not work.

## The versioning conundrum

At that stage we had three options to handle those projects switching from
one model to another. They could keep their 2015.2.0 version and start doing
semantic versioning from that -- but that would be highly confusing, when you
end up releasing 2017.9.4 sometimes in 2016. The second option was to reset
the version for projects as they switch. So Ironic would adopt, say, 3.0.0
while all other projects still use 2015.2.0.

The third option was to bite the bullet and drop the YEAR.N versioning at the
same time, for all the projects that were still using it. Switching
them all to some arbitrary number (say, 12.0.0 since that would be the 12th
OpenStack release) would create confusion as projects switching to
intermediary releases would slowly drift from the pack (most projects
publishing 13.0.0 while some would be at 12.5.2 and others at 13.1.0).
So to avoid that confusion, projects would pick purposefully distinct version
numbers based on their age.

## The change

After discussions at the Vancouver Design Summit and on the mailing-list,
we opted for the third option, with an initial number calculated from the
number of past integrated releases already published.

It's a clean cut which will reduce on-going disruption. All components end
up with a different, meaningful version number: there are no longer "normal"
and "outliers" projects. Additionally, it solves the weird impression we had
when we released 2014.2.2 stable versions sometimes in 2015.

As far as impact is concerned, distributions will need to make sure to insert
an *epoch* so that package versions sort correctly in their package management
systems. If your internal CI pipeline relies on sorting version numbers, it
will likely need an adjustment too. For everyone else, it should not have an
impact: when Liberty is out, you will upgrade to the liberty version of the
components, as you always did.

## Liberty-1 and the future

The change in versions was pushed last week, and that is why for liberty-1 we
published 12.0.0.0b1 for Nova, 8.0.0.0b1 for Keystone, and 1.0.0.0b1 for
Designate, etc... Those are still on a milestone-based 6-month release cycle,
but their "Liberty" final version won't be all versioned "2015.2.0", but 12.0.0
for Nova, 8.0.0 for Keystone, etc.

To reduce the confusion, the release management team will provide tooling and
web pages to describe what each series means in terms of component version
numbers (and the other way around).

We hope this future-proof change will bring some more freedom for OpenStack
project teams to pick the release model that is the most interesting for them
and their user base. For a cycle named "liberty", that sounded like a pretty
good time to do it.

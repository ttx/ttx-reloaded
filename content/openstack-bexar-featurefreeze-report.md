Title: OpenStack Bexar FeatureFreeze report
Date: 2011-01-14 08:44
Author: Thierry Carrez
Tags: OpenStack
Slug: openstack-bexar-featurefreeze-report

The OpenStack Bexar release now
passed [FeatureFreeze](http://wiki.openstack.org/FeatureFreeze).
Branches containing needed new features or changing the expected
behavior of the software can still require an exception and be proposed,
but their benefit will have to outweigh the regression risks they bring
for them to be part of the Bexar release.

Some insight on how well we managed to hit the objectives of this
deadline (% of specs that were merged in time for the freeze):

-   Essential specs: 3 merged (100%)
-   High-prio specs: 14 merged, 1 still proposed (93%)
-   Medium-prio specs: 9 merged, 2 still proposed, 4 deferred (60%)
-   Low-prio specs: 8 merged, 2 still proposed, 2 deferred (66%)

So we did a great job of getting High-prio proposed branches merged.
Thanks to a final push on the freeze day, we also managed to get most of
the Medium and Low priority branches in. A few previously-untargeted
branches made it, like [switching to CoW format by
default](https://blueprints.launchpad.net/nova/+spec/cow-instances),
support for [availability
zones](https://blueprints.launchpad.net/nova/+spec/instance-avail-zones)
or [CEPH
volumes](https://blueprints.launchpad.net/nova/+spec/ceph-block-driver),
for a total of [45 targeted
specs](http://wiki.openstack.org/releasestatus/). The overall hit score
is just above 75%, which is amazing for that number of objectives.

Next stop is in 12
days, [GammaFreeze](http://wiki.openstack.org/GammaFreeze) (Jan 25).
Until then, we need to get as many bugfixes in as possible. Now that
(most) feature branches have landed, it's time to put your QA suit on
and test, report and fix all issues you encounter. Let's make Bexar a
great release !

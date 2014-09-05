Title: OpenStack Bexar BMPFreeze report
Date: 2011-01-07 14:00
Author: Thierry Carrez
Tags: OpenStack
Slug: openstack-bexar-bmpfreeze-report

The OpenStack Bexar release now passed
[BranchMergeProposalFreeze](http://wiki.openstack.org/BranchMergeProposalFreeze).
Branches containing new features or changing the behavior of the
software can still require an exception and be proposed, but there is no
guarantee they will be accepted and be part of the Bexar release.

Some insight on how well we managed to hit the objectives of this
deadline (% of specs that were proposed in time for the freeze):

-   Essential specs: 3 merged (100%)
-   High-prio specs: 8 merged, 5-6 proposed, 2-1 late (87-93%)
-   Medium-prio specs: 5 merged, 4 proposed, 3 late, 3 deferred (60%)
-   Low-prio specs: 2 merged, 4 proposed, 3 late (66%)

Given the very high number of specs targeted to Bexar, this is quite
good (I was expecting something around 100%, 75%, 50% and 25%). The
overall score is around 75%, which is amazing with [42 targeted
specs](http://wiki.openstack.org/releasestatus/) in 3 months. Congrats
to all the developers ! We also had a few unexpected specs that made it,
we will retrospectively add them to the picture.

Next stop is next week,
[FeatureFreeze](http://wiki.openstack.org/FeatureFreeze) (Jan 13): all
feature branches need to be merged so that we can safely switch to
QA/testing/bugfix gear, 3 weeks away from release. Given how well the
reviews go, I hope we will be able to sneak a few late branches in and
further improve the scores.

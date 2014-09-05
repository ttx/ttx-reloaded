Title: Getting to Havana
Date: 2013-10-18 13:43
Author: Thierry Carrez
Tags: OpenStack
Slug: getting-to-havana

Yesterday, as the final conclusion of the 6-month "Havana" development
cycle, we [released the latest version of
OpenStack](http://lists.openstack.org/pipermail/openstack-announce/2013-October/000151.html),
the 2013.2 version. It's now composed of 9 integrated components, which
saw the completion of more than 400 feature blueprints and the fixing of
more than 3000 reported bugs.

As always, it's been an interesting week for me. Not as busy as you'd
think, but lots of hours, day or night, spent frantically checking
dashboards, collecting input from our fearful technical leads, waiting
for a disaster to happen and pushing the right buttons at the right
moment, finally aligning the stars and releasing everything on time.
Yes, I use checklists to make sure I don't overlook anything:

 

![havana cheat sheet]({filename}/images/havana-cheatsheet.jpg)

 

Even if I have plenty of free time between those key hours, I can't
concentrate on getting anything else done, or get something else started
(like a blog post). This is why, one day after release, I can finally
spend some time looking back on the last stage of the Havana development
cycle and see how well we performed. Here is the graph showing the
number of release-critical bugs logged against various components (those
observing the common feature freeze) as we make progress towards the
final release date:

 

![havana RCs]({filename}/images/havana-rcs.png)

 

Personally I think we were a bit late, with RC1s globally landing around
October 3 and RC2s still being published around October 15. I prefer
when we can switch to "respin only for major regressions and upgrade
issues" mode at least a week before final release, not two days before
final release. Looking at the graph, we can see where we failed: it took
us 11 days to get a grip on the RC bug count (either by fixing the right
issues, or by stopping adding new ones, or by refining the list and
dropping non-critical stuff). Part of this delay is due to stress
recovery after a rather eventful feature freeze. Part of it is lack of
prioritization and focus on the right bugs. The rest of the graph pretty
much looks like [the Grizzly
one]({filename}/images/grizzly-rcs.png). We were
just at least one week too late.

We'll explore ways to improve on that during the Icehouse Design Summit
in Hong-Kong. One solution might be to add a week between feature freeze
and final release. Another solution would be to filter what gets
targeted to the last milestone to reduce the amount of features that
land late in the cycle, to reduce FeatureFreeze trauma. If you want to
be part of the discussion, [join us all in
Hong-Kong](http://www.openstack.org/summit/openstack-summit-hong-kong-2013)
in 18 days !

 

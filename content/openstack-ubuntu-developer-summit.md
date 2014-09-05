Title: OpenStack @ Ubuntu Developer Summit
Date: 2011-05-18 12:53
Author: Thierry Carrez
Tags: OpenStack
Slug: openstack-ubuntu-developer-summit

Last week I attended the [Ubuntu Developer Summit for
Oneiric](http://uds.ubuntu.com/) in Budapest. This was the first time I
attended UDS as an upstream representative rather than as a Canonical
employee. I very much enjoyed it: not being a track lead or a busy
technical lead actually gives you desirable flexibility in your agenda
:)

First of all, a quick comment on the big announcement of the week, which
the Twittersphere is not done retweeting yet: "Ubuntu switching from
Eucalyptus to OpenStack". I think it would be more accurate to say that
Ubuntu chose to use OpenStack as its *default* cloud stack for future
versions. Comparing Eucalyptus and OpenStack is like comparing apples to
apple trees: OpenStack provides several cloud infrastructure pieces (of
which only OpenStack Compute -Nova- covers the same space as
Eucalyptus). I suspect the wide scope of the project played a role in
OpenStack being selected as the default stack for the future. Eucalyptus
and OpenStack Nova should both be present as deployment options from
11.10 on.

On the UDS format itself, I'd say that the "one blueprint = one hour"
format does not scale that well. The numbers of hours in the week is
fixed, so when the project grows you end up having too many sessions
going on at the same time. Lots of blueprints do not require one hour of
discussion, but rather a quick presentation of plan, feedback from
interested parties and Q&A. That's what we do for our own Design
Summits, but I'd admit it makes scheduling a bit more complex. On the
good side, having the floor plan inside our UDS badges was a really good
idea, especially with confusing room names :)

The Launchpad and bzr guys were very present during the week, attentive
and reactive to the wishes of upstream projects. They have great
improvements and features coming up, including [finer-grained
bugmail](http://blog.launchpad.net/bug-tracking/beta-squadron-engage-better-bug-subscriptions)
and dramatic [speed
improvements](http://bazaarvcs.wordpress.com/2011/05/17/faster-large-tree-handling/)
in bzr handling of large repos.

Last week also saw the rise of creampiesourcing: motivation of groups of
developers over bets ("if the number of critical bugs for Launchpad goes
to 0 by June 27, I'll [take a
creampie](http://blog.launchpad.net/general/a-cream-pie-in-the-face)in
the face"). Seems to work better than karma points.

Finally, Rackspace Hosting was co-sponsoring the "meet and greet" event
on the Monday night, promoting OpenStack. I think offering cool
T-shirts, like we did at the previous UDS in Orlando, was more efficient
in spreading the word and making the project "visible" over time: in
Budapest you could see a lot of people wearing the OpenStack T-shirts we
offered back then !

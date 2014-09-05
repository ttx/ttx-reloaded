Title: The need for releases
Date: 2013-04-11 14:32
Author: Thierry Carrez
Tags: Open source, OpenStack, Popular
Slug: the-need-for-releases

The beginning of a new release cycle is as good as any moment to
question why we actually go through the hassle of producing OpenStack
releases. [Twice per
year](https://wiki.openstack.org/wiki/Release_Cycle), on a precise date
we announce 6 months in advance, we bless and publish source code
tarballs of the various integrated projects in OpenStack. Every week we
have a
[meeting](https://wiki.openstack.org/wiki/Meetings/ProjectMeeting) that
tracks our progress toward this common goal. Why ?

### Releases vs. Continuous deployment

The question is particularly valid if you take into account the type of
software that we produce. We don't really expect cloud infrastructure
providers to religiously download our source code tarballs every 6
months and run from that. For the largest installations, running much
closer to the master branch and continuously deploy the latest changes
is a really sound strategy. We invested a lot of effort in our gating
systems and QA automated testing to make sure the master branch is
always runnable. We'll discuss at the [OpenStack
Summit](http://www.openstack.org/summit/portland-2013/) next week how to
improve CD support in OpenStack. We backport bugfixes to the [stable
branches](https://wiki.openstack.org/wiki/StableBranch) post-release. So
why do we continue to single out a few commits and publish them as "the
release" ?

### The need for cycles

The value is not really in *releases*. It is in *release cycles*.

Producing OpenStack involves the work of a large number of people. While
most of those people are paid to participate in OpenStack development,
as far as the OpenStack project goes, we don't manage them. We can't ask
them to work on a specific area, or to respect a given deadline, or to
spend that extra hour to finalize something. The main trick we use to
align everyone and make us all part of the same community is to have a
cycle. We have regular milestones that we ask contributors to target
their features to. We have a [feature
freeze](https://wiki.openstack.org/wiki/FeatureFreeze) to encourage
people to switch their mindset to bugfixing. We have weekly meetings to
track progress, communicate where we are and motivate us to go that
extra mile. The common rhythm is what makes us all play in the same
team. The "release" itself is just the natural conclusion of that common
effort.

### A reference point in time

Singling out a point in time has a number of other benefits. It's easier
to work on documentation if you group your features into a coherent set
(we actually considered shortening our cycles in the past, and the main
blocker was our capacity to produce good documentation often enough).
It's easier to communicate about OpenStack progress and new features if
you do it periodically rather than continuously. It's easier to have
[Design Summits](https://wiki.openstack.org/wiki/Summit) every 6 months
if you create a common brainstorm / implementation / integration cycle.
The releases also serve as reference points for API deprecation rules,
for stable release maintenance, for security backports.

If you're purely focused on the software consumption part, it's easy to
underestimate the value of release cycles. They actually are one of the
main reasons for the pace of development and success of OpenStack so
far.

### The path forward

We need release *cycles*... do we need release *deliverables* ? Do we
actually need to bless and publish a set of source code tarballs ? My
personal view on that is: if there is no additional cost in producing
releases, why not continue to do them ? With the release tooling we have
today, blessing and publishing a few tarballs is as simple as pushing a
tag, running a script and sending an email. And I like how this formally
concludes the development cycle to start the stable maintenance period.

But what about Continuous Deployment ? Well, the fact that we produce
releases shouldn't at all affect our ability to continuously deploy
OpenStack. The master branch should always be in good shape, and we
definitely should have the necessary features in place to fully support
CD. We can have both. So we should have both.

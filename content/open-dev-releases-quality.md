Title: Open development, releases and quality
Date: 2012-02-21 14:07
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: open-dev-releases-quality

Every 6 months, as a cycle ends and we prepare the next, we look back at
our release model and try to see how we can improve it. My opinion is
that we need (once more) to evolve it, and here is why.

#### Objectives and past evolutions

Our main objective is to produce stable and usable software. Our
secondary objective is let stable new features reach the hands of our
users in a timely manner. Our tertiary objective is to empower
developers to work efficiently on the features and improvements of
tomorrow. In simple solutions, those three objectives are not really
compatible, and in the past we tried to make adjustments without
acknowledging the fundamental incompatibility between those objectives.

The [Austin-Cactus
system](http://wiki.openstack.org/CactusReleaseSchedule) was a 3-month
cycle with various freezes. The issues with this system were that it
took too long to get features in the hands of testers and users,
developers had trouble working during the frozen periods, and not so
many people actually helped during the QA period.

For [Diablo](http://wiki.openstack.org/DiabloReleaseSchedule), we
decided to switch to a 6-month cycle with monthly milestones. Those
milestones were supposed to address the "get features into the hands of
users early" issue. To empower developers, we introduced an
almost-always-open trunk: we only had 2 weeks of feature freeze before
the Essex branch opened (and coexisted with the Diablo release branch).
The problem was the resulting quality was not good, since we accumulated
6 months' worth of features and only had 2 weeks' worth of QA on them.

So for [Essex](http://wiki.openstack.org/EssexReleaseSchedule), there
was a decision that each project would decide where to place its feature
freeze and its first release candidate (which would be when the Folsom
branch opens). Most of them decided to use the essex-3 milestone as a
soft feature freeze and essex-4 as a hard one, which reintroduced the
"closed trunk" issue. And the work needed to stabilize 6 months' worth
of features is still daunting. And we saw lots of feature freeze
exceptions for last-minute "almost there" features that can't afford to
wait another 6 months.

So what's the solution ? Is there a good way to (at the same time)
reduce the pain of "missing a release", have always-open development
branches, and get higher quality ?

#### The kernel model

The only way to reduce the pain of missing a release is to have shorter
time-based releases. The only way to have always-open development
branches without sacrificing release quality is to separate them
completely from release branches. Where do those truisms lead us ?

Another famous open innovation project has already been there, and
that's the Linux kernel. Development happens in various always-open
topic branches, and regularly a merge window opens to propose stable
features for inclusion in the mainline kernel.

If we manage to efficiently separate OpenStack in topics, we could adopt
the same model. We could have several topic branches where core
developers on a specific area can collaborate and review code affecting
that area. We could have frequent releases (every 6-8 weeks ?), and for
each release we could have a "merge window" where stuff from topic
branches can be proposed for release, if deemed stable enough. Between
the moment the merge window closes and the moment the final release is
cut, various release candidates can be produced, on which serious QA can
be unleashed without blocking other developers.

This solves all objectives. If a feature is not ready yet (according to
the team maintaining the topic branch or according to release
management), it can bake until the next merge window, which is not far
away. Regular releases ensure that improvements reach the users in a
timely manner. Development branches are always open. And with a
reasonable amount of new code in every release, QA work is facilitated,
theoretically resulting in higher release quality.

#### Additional benefits

Splitting development into topics has an additional benefit: smaller
groups developing an expertise on a specific area make better reviewers
on that specific area than a random nova-core developer that can't be an
expert in all things Nova. I'd say that each topic should be small
enough to be manageable with a team of 6 core reviewers at the maximum.
Of course, nothing prevents anyone from being active on multiple topics
if they wish.

More frequent releases also allows you to set themes for each release.
It's difficult to refuse some feature in a 6-month cycle, but it's easy
to delay a feature to the next 6-week cycle. In the same way some kernel
releases introduce large architectural changes and some others are more
geared towards performance improvements or stability, we could also
define themes for every release -- after all the next one is not so far
away.

#### Challenges

There are a few issues with this model obviously. Code needs to be
componentized enough so that merge pains can be limited. Changes from
every release need to be merged back into topic branches. Code needs to
be clearly separated into a set of relevant topics, each with its own
set of core reviewers maintaining the topic branch. The release team
must be staffed enough to be able to review proposed code for stability.
Bug fixes need to easily end up in the release branch. And how do those
"releases" match the 6-month period between summits ? What means
"Folsom" in that respect ?

I hope we can use the following weeks to discuss the devil in the
details of this possible evolution, and be ready to take a decision when
the time comes for us to gather at the Folsom Design summit.

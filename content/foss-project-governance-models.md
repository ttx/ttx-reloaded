Title: F/OSS project governance models
Date: 2014-04-23 13:39
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: foss-project-governance-models

Various governance models exist for free and open source software
projects. Most of those happen naturally, some of them are chosen...
Which one is the best ? Is there a best ? How could we judge the best ?
Like any ecosystem, I'd postulate that F/OSS project communities should
have long-term survival as their main goal: the ability to continue
operation as the same community over time, without fracture of fork.

### Dictatorship

The "benevolent dictator for life" model usually happens naturally. The
project is often originally the brain child of a single, talented
individual, who retains final say over everything that happens to
*their* project. This usually works very well: the person is naturally
respected in the community. It also naturally allows for opinionated
design, and people who sign up to the project can't ignore what they
sign up for.

The main issue with that setup is that it's not replicable, it can't be
dictated. It either happens naturally, or it will never happen. You
don't choose someone to become your dictator-for-life after the fact.
Any attempt to do so would fail to get enough legitimacy and natural
respect to make it last. The second issue with that setup is that it's
not durable. If the dictator stops being active in the community, their
opinion is not as much respected anymore (especially by new
contributors), which usually triggers a painful fork or governance model
switch (that's what happened in Gentoo). Even in the rare cases where
the original dictator manages to retain interest and respect in the
project, it's inherently brittle: the "natural" dictator can't really be
replaced in case something bad happens. Succession is always dirty. So
from a long-term survival standpoint, this model is not that great.

### Aristocracy

Aristocracy is used to solve the perceived drawbacks of the
dictator-for-life model. Instead of focusing on one person, let's have a
group of people in control of the project, and let that group
self-select successors in the wider pool of contributors. That's the
role of "committers" in certain projects, and it's also how Apache
project management committees (PMCs) usually work. It also works quite
well, with self-selection usually ensuring that the members share enough
common culture to reach consensus on most decisions.

The drawback here is obviously the self-selection bias. Aristocracies
all fall after getting more and more disconnected from the people they
control, and revolution happens. Open source aristocracies are no
different: they fall after gradually growing disconnected from their
project contributors base. Whenever contributors to an open source
project feel like their leaders are no longer representative of the
contributors or relevant to the present of the project, this disconnect
happens. In mild cases, people just go contribute somewhere else, and in
difficult cases this usually triggers a fork.

### Direct democracy / Anarchy

The obvious way to solve that disconnect is to give the power directly
to the contributors. Direct democracy projects give ultimate power to
all the contributors. Anarchy projects let contributors do whatever they
want. Debian is an interesting mix of the two: developers vote on
general resolutions, but maintainers also have a lot of control on their
packages.

While these models have a certain appeal, those projects usually have a
hard time taking necessary decisions that affect the whole project, so
they tend to linger not taking any critical decision. It's also a model
that is difficult to evolve: when you try to add new layers on top of
it, they are never really accepted by the contributors base.

### Representative democracy

That leaves us with representative democracy. You regularly designate a
small group of people and trust them to make the right decisions for the
governance of the project. It can happen in cases where there was no
natural dictator at the beginning of the project. It's different from
aristocracy in that they are chosen by the contributors base and
regularly renewed -- ensuring that they are always seen as a fair
representation of the contributors to the project. It's more efficient
than direct democracy or anarchy in making clear and opinionated
decisions.

Now it's far from perfect. As Churchill famously said, *it's the worst
form of government, except all those other forms that have been tried
from time to time*. It also only works if the elected people are seen as
legitimate and representative, so it requires good participation levels
in elections. So here is my plea: the OpenStack Technical Committee,
which oversees the development of the OpenStack open source project as a
whole, is being partially renewed this week. If you're an OpenStack
contributor, please vote: this will ensure that elected people have the
legitimacy necessary for making the decisions that need to be made, and
increase the health of the project.

 

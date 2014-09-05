Title: The dilemma of open innovation
Date: 2014-02-24 14:44
Author: Thierry Carrez
Tags: Open source, Openstack, Popular
Slug: the-dilemma-of-open-innovation

## Open innovation vs. proprietary innovation

For companies, there are two ways to develop open source projects. The
first one is to keep design and innovation inside your corporate
borders, and only accept peripheral contributions. In that case you
produce open source software, but everything else resembles traditional
software development: you set the goals and roadmap for your product,
and organize your development activity to meet those goals, using Agile
or waterfall methodologies.

The second one is what we call *open innovation*: build a common and
level playing field for contributions from anywhere, under the auspices
of an independent body (foundation or other). In that case you don't
really have a roadmap: what ends up in the software is what the
contributors manage to push through a maintainers trust tree (think: the
Linux kernel) or a drastic code review / CI gate (think: OpenStack).
Products or services are generally built on top of those projects and
let the various participants differentiate on top of the common
platform.

Now, while I heavily prefer the second option (which I find much closer
to the ideals of free software), I recognize that both options are valid
and both are open source. The first one ends up attracting far less
contributions, but it works quite well for niche, specialized products
that require some specific know-how and where focused product design
gives you an edge. But the second works better to reach universal
adoption and total world domination.

## A tragedy of the commons

The dilemma of open innovation is that it's a natural tragedy of the
commons. You need strategic contributions to keep the project afloat:
people working on project infrastructure, QA, security response,
documentation, bugfixing, release management which do not directly
contribute to your employer baseline as much as a tactical contribution
(like a driver to interface with your hardware) would. Some companies
contribute those necessary resources, while some others just get the
benefits of monetizing products or services on top of the platform
without contributing their fair share. The risk, of course, is that the
strategic contributor gets tired of paying for the free rider.

Open innovation is a living ecosystem, a society. Like all societies, it
has its parasites, its defectors, those which don't live by the rules.
And like all societies, it actually *needs* a certain amount of
defectors, as it makes the society stronger and more able to evolve. The
trick is to keep the amount of parasites down to a tolerable level. In
our world, this is usually done by increasing the difficulty or the cost
of defecting, while reducing the drawbacks or the cost of cooperating.

## Keeping our society healthy

In his book *Liars and Outliers*, Bruce Schneier details the various
knobs a society can play with to adjust the number of defectors. There
are moral pressures, reputational pressures, institutional pressures and
security pressures. In open innovation projects, moral pressures and
security pressures don't work that well, so we usually use a combination
of institutional pressures (licensing, trademark rules) and reputational
pressures (praising contributors, shaming free riders) to keep defectors
to an acceptable level.

Those are challenges that are fully understood and regularly applied in
the Linux kernel project. For OpenStack, the meteoritic growth of the
project (and the expertise land-grab that came with it) protected us
from the effects of the open innovation dilemma so far. But the
Technical Committee shall keep an eye on this dilemma and be ready to
adjust the knobs if it starts becoming more of a problem. Because at
some point, it will.

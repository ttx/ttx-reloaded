Title: The Age of Foundations
Date: 2015-07-29 15:30
Author: Thierry Carrez
Tags: OpenStack, Open source
Slug: the-age-of-foundations


At OSCON last week, Google announced the creation around Kubernetes of the
Cloud-Native Computing Foundation. The next day, Jim Zemlin dedicated his
keynote to the (recently-renamed) Open Container Initiative, confirming the
Linux Foundation's recent shift towards providing Foundations-as-a-Service.
Foundations ended up being the talk of the show, with some questioning the
need for Foundations for everything, and others discussing the rise of
Foundations as tactical weapons.

## Back to the basics

The main goal of open source foundations is to provide a neutral, level and
open collaboration ground around one or several open source projects. That is
what we call the **upstream** support goal. Projects are initially created by
individuals or companies that own the original trademark and have power to
change the governance model. That creates a tilted playing field: not all
players are equal, and some of them can even change the rules in the middle
of the game. As projects become more popular, that initial parentage becomes
a blocker for other contributors or companies to participate. If your goal is
to maximize adoption, contribution and mindshare, transferring the ownership
of the project and its governance to a more neutral body is the natural next
step. It removes barriers to contribution and truly enables open innovation.

Now, those foundations need basic funding, and a common way to achieve that
is to accept corporate members. That leads to the secondary goal of open source
foundations: serve as a marketing and business development engine for companies
around a common goal. That is what we call the **downstream** support goal.
Foundations work to build and promote a sane ecosystem around the open source
project, by organizing local and global events or supporting initiatives to
make it more usable: interoperability, training, certification, trademark
licenses...

## Not all Foundations are the same

At this point it's important to see that a foundation is not a label, the
name doesn't come with any guarantee. All those foundations are actually very
different, and you need to read the fine print to understand their goals or
assess exactly how open they are.

On the upstream side, few of them actually let their open source project be
completely run by their individual contributors, with elected leadership
(one contributor = one vote, and anyone may contribute). That form of
governance is the only one that ensures that a project is really open to
individual contributors, and the only one that prevents forks due to
contributors and project owners not having aligned goals. If you restrict
leadership positions to appointed seats by corporate backers, you've created
a closed pay-to-play collaboration, not an open collaboration ground. On the
downstream side, not all of them accept individual members or give
representation to smaller companies, beyond their founding members.
Those details matter.

When we set up the OpenStack Foundation, we worked hard to make sure we
created a solid, independent, open and meritocratic *upstream* side. That,
in turn, enabled a pretty successful *downstream* side, set up to be inclusive
of the diversity in our ecosystem.

## The future

I see the "Foundation" approach to open source as the only viable solution
past a given size and momentum around a project. It's certainly preferable
to "open but actually owned by one specific party" (which sooner or later
leads to forking). Open source now being the default development model in
the industry, we'll certainly see even more foundations in the future, not
less.

As this approach gets more prevalent, I expect a rise in more tactical
foundations that primarily exist as a trade association to push a specific
vision for the industry. At OSCON during those two presentations around
container-driven foundations, it was actually interesting to notice not the
common points, but the differences. The message was subtly different (pods
vs. containers), and the companies backing them were subtly different too.
I expect differential analysis of Foundations to become a thing.

My hope is that as the "Foundation" model of open source gets ubiquitous,
we make sure that we distinguish those which are primarily built to sustain
the needs or the strategy of a dozen of large corporations, and those which
are primarily built to enable open collaboration around an open source project.
The *downstream* goal should stay a secondary goal, and new foundations need
to make sure they first get the *upstream* side right.

In conclusion, we should certainly welcome more Foundations being created to
sustain more successful open source projects in the future. But we also need
to pause and read the fine print: assess how open they are, discover who ends
up owning their upstream open source project, and determine their primary
reason for existing.

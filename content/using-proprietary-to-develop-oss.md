Title: Using proprietary services to develop open source software
Date: 2017-02-19 14:00
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: using-proprietary-to-develop-oss

It is now pretty well accepted that open source is a superior way of
producing software. Almost everyone is doing open source those days.
In particular, the ability for users to look under the hood and make
changes results in tools that are better adapted to their workflows.
It reduces the cost and risk of finding yourself locked-in with a vendor
in an unbalanced relationship. It contributes to a virtuous circle of
continuous improvement, blurring the lines between consumers and producers.
It enables everyone to remix and invent new things. It adds up to the
common human knowledge.

### And yet

And yet, a lot of open source software is developed on (and with the help
of) proprietary services running closed-source code. Countless open source
projects are developed on GitHub, or with the help of Jira for bugtracking,
Slack for communications, Google docs for document authoring and sharing,
Trello for status boards. That sounds a bit paradoxical and hypocritical --
a bit too much "do what I say, not what I do". Why is that ? If we agree
that open source has so many tangible benefits, why are we so willing to
forfeit them with the very tooling we use to produce it ?

### But it's free !

The argument usually goes like this: those platforms may be proprietary, they
offer great features, and they are provided free of charge to my open source
project. Why on Earth would I go through the hassle of setting up,
maintaining, and paying for infrastructure to run less featureful solutions ?
Or why would I pay for someone to host it for me ? The trick is, as the
saying goes, when the product is free, **you** are the product. In this case,
your open source community is the product. In the worst case scenario, the
personal data and activity patterns of your community members will be sold
to 3rd parties. In the best case scenario, your open source community is
recruited by force in an army that furthers the network effect and makes it
even more difficult for the next open source project to not use that
proprietary service. In all cases, you, as a project, decide to not bear the
direct cost, but ask each and every one of your contributors to pay for it
indirectly instead. You force all of your contributors to accept the
ever-changing terms of use of the proprietary service in order to participate
to your "open" community.

### Recognizing the trade-off

It is important to recognize the situation for what it is. A trade-off.
On one side, shiny features, convenience. On the other, a lock-in of your
community through specific features, data formats, proprietary protocols or
just plain old network effect and habit. Each situation is different. In
some cases the gap between the proprietary service and the open platform
will be so large that it makes sense to bear the cost. Google Docs is pretty
good at what it does, and I find myself using it when collaborating on
something more complex than etherpads or ethercalcs. At the opposite end of
the spectrum, there is really **no** reason to use Doodle when you can use
[Framadate](https://framadate.org). In the same vein, [Wekan](https://wekan.io)
is close enough to Trello that you should really consider it as well.
For Slack vs. [Mattermost](https://about.mattermost.com) vs. IRC, the
trade-off is more subtle. As a sidenote, the cost of lock-in is a lot
reduced when the proprietary service is built on standard protocols. For
example, GMail is not that much of a problem because it is easy enough to
use IMAP to integrate it (and possibly move away from it in the future).
If Slack was just a stellar opinionated client using IRC protocols and
servers, it would also not be that much of a problem.

### Part of the solution

Any simple answer to this trade-off would be dogmatic. You are not unpure
if you use proprietary services, and you are not wearing blinders if you
use open source software for your project infrastructure. Each community
will answer that trade-off differently, based on their roots and history.
The important part is to acknowledge that nothing is free. When the choice
is made, we all need to be mindful of what we gain, and what we lose.
To conclude, I think we can all agree that all other things being equal, when
there is an open-source solution which has all the features of the
proprietary offering, we all prefer to use that. The corollary is, we all
benefit when those open-source solutions get better. So to be part of the
solution, consider helping those open source projects build something as
good as the proprietary alternative, especially when they are pretty close
to it feature-wise. That will make solving that trade-off a lot easier.

Title: Agile vs. Open
Date: 2011-01-21 10:53
Author: Thierry Carrez
Tags: Open source, OpenStack, Popular
Slug: agile-vs-open

I've been asked multiple times why open source project management does
not fully adopt agile methodologies, which are so great. Or what are the
main differences between the two.

## Agile is good for you

So first of all, I'd like to say that I think Agile methodologies are
great. Their primary value to me is to allow software development groups
to handle their stakeholders requirements in a sane way. By involving
developers more in the center of game, they contribute to use *Autonomy*
(one of the three main intrinsic motivators that Dan Pink mentions in
his book *Drive*) as a way to maximize a development team productivity.

## Agile vs. Open

That said, applying pure Agile methods doesn't really work well for open
source project management. Some great concepts can be reused, like
frequent time-based releases, peer review, or test-driven development.
But most of the group tools assume a local, relatively small team. Doing
a morning stand-up meeting with a team of 60 in widely different
timezones is a bit difficult. It also assumes that project management
has some direct control over the developers (they can pick in the
backlog, but not outside), while there is no such thing in an open
development project.

The goals are also different. The main goal of Agile in my opinion is to
maximize a development team productivity. Optimizing the team velocity
so that the most can be achieved by a given-size team. The main goal of
Open source project management is not to maximize productivity. It's to
**maximize contributions**. Produce the most, with the largest group of
people possible.

That's why open source project management is all about setting the
framework and the rules of play (what can get in trunk and how), and
about trying to keep track of what is being done (to minimize confusion
and friction between groups of developers). That's why our release
cycles are slightly longer than Agile sprints, to have a cadence that is
more inclusive of development styles, and to enforce time to focus, as a
group, on QA before a release.

## Agile devs in Open source

It's difficult for Agile developers to abandon their nice tools and
adopt seemingly-more-confusing open source bazaar ways. But in the end,
I think open source is more empowering, by addressing the two other Dan
Pink types of intrinsic motivators, *Purpose* and *Mastery*. Working on
an open source project and contributing to the world's amount of public
knowledge obviously gives an individual a sense of purpose to his work,
but even more important is mastery.

Each developer in an open source project actually represents himself.
With all proceedings and production being public, in the end his
personal name is attached to it. He builds mastery and influence over
the project by his own actions, not by the name of the company that pays
his bills. Of course his employer has requirements and usually pays him
to work on something specific, but the developer acts as the gateway to
get his employer's requirements into the open source project. That way
of handling stakeholders requirements places individual developers at
the very center of the game, even more than Agile does. You end up with
the highest number of highly-motivated individuals, which in turn leads
to lots of stuff getting done.

## Agile subteams

Finally, nothing prevents an open source project to have Agile
development subgroups contributing to it. These subgroups can have user
stories, planning poker, feature backlogs, pair programming and stand-up
meetings. There are multiple challenges though. Aligning agile sprints
with the open source project's common development schedule is tricky.
The Agile work schedule needs to be adapted to make room for generic
open source project tasks like random code reviews or pre-release QA.
Some other group may end up implementing a feature from your internal
backlog, and communicating the backlog outside the group can be
bothersome and challenging.

I'd like to find ways, though. What do you think ? Can Agile and Open
live in harmony ? Should they try ?

Title: The next step for OpenStack
Date: 2011-09-28 12:13
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: the-next-step-for-openstack

Just after a release, discovery of significant bugs always revives
discussion around the need for maintenance branches or point releases.
Those discussions, however, are not solving the root cause for the
issue, but merely try to do damage control on the consequences.

The root cause for presence of significant bugs in a given release is
not the presence or absence of maintenance branches. It's not about the
choice of time-based cycles, or the length of it. It's about lack of
focus on testing and fixing the release deliverables. If only a few
people work on that, while all the others are busy adding new features
in trunk, delaying your release by one or more weeks won't change
anything.

### From tactical to strategic contributions

OpenStack is one of the few open source projects where development is
truly shared across multiple companies. The trick is, most companies
involved so far are doing what I call *tactical contributions*: adding a
feature that they care about, fix bugs that affect them. Tactical
contributions are great to expand a project scope, community and
mindshare, however they add technical debt. Companies involved need to
move to what I call *strategic contributions*: funding development
resources that care about the end result, the release deliverables, the
absence of bugs, the coherence of the features.

The obvious comparison point is the Linux kernel. The reason why it's
successful, despite lots of companies only involved in tactical
contributions, is that at its core it has a strong group of key
developers whose primary allegiance goes to the Linux kernel itself, no
matter what company they happen to work for. Those companies understood
the necessity of funding strategic contributions.

Currently, especially in Nova, it's quite difficult to get merge
proposals reviewed, random bugs fixed, integration tests contributed, or
holes in scope covered. That's because most groups are focused on their
own objectives, rather than the common project objectives. That's the
mindset we need to change now, and that's the only thing that can give
us better releases.

### The cost of strategic contributions

The problem with strategic contributions is that they are typically more
costly than tactical contributions, which have a more obvious return on
investment. Accepting to have developers on payroll "fixing what needs
to be fixed", or giving 30% free time to all your developers so that
they can work on project objectives rather than only your own is not
that easy. But OpenStack has now proven that it's here to stay, lots of
companies have now bet their strategy on it, so I think the time is now.

If we don't adjust, OpenStack in general (and Nova in particular) will
crumble under the technical debt of tactical contributions, and everyone
involved will lose. We might need to adjust governance to encourage
other companies to invest long-term in project-centered resources. We'll
need to set up open, multi-company workgroups (like the recently-setup
QA team) to clearly show that it's a common effort. It won't happen in a
day, but if we don't change our mindset now, no matter how we adjust the
release cycle, Essex deliverables will be of the same quality as Diablo.

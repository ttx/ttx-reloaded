Title: Upstream projects vs. Distributions
Date: 2011-02-28 11:08
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: upstream-projects-vs-distributions

You can globally split open source projects into two broad categories.
*Upstream* projects develop and publish source code for various
applications and features. *Downstream* projects are consumers of this
source code. The most common type of downstream projects are
*distributions*, which release ready-to-use binary packages of these
upstream applications, make sure they integrate well with the rest of
the system, and release security and bugfix updates according to their
maintenance policies.

The relationship between upstream projects and distributions is always a
bit difficult, because their roles overlap a bit. Since I'm sitting on
both sides of the fence, let's try to find common ground.

### Overlapping roles

In an ideal world, everyone would install software through distribution
packages, and the roles wouldn't overlap. In the real world though,
upstream projects need to deal with distributions that don't provide
packages for your software, or provide old buggy versions with no
mechanism for getting fresh ones. That's why they need to care about
manual installation or update mechanisms. On the other hand, in their
rush to release fixes, distributions sometimes carry patches without
sending them upstream immediately. Both want to provide bugfix updates
to stable versions. In all cases the overlapping roles end up
duplicating work and creating unnecessary friction.

### Splitting the roles

In my (humble) opinion, upstream projects should encourage the use of
packaged software wherever possible, rather than resisting it. They
should concentrate on their core competency: working on producing new
releases of their code. Dealing with distribution issues, environment
specificities or maintaining stable branches is a different type of
work, and one that distributions excel in. So the key seems to be in
splitting the roles more cleanly.

Upstream projects should release code, together with good documentation
on how to manually deploy it: dependencies, startup and upgrade
mechanisms, open bug trackers with links to patches... This
documentation can be reused by manual deployers and distribution
packagers alike. They should stop short of providing installers,
auto-updaters, dependency bundles, etc. They should limit the release of
point release updates only to critical issues (data loss, security...).

Distributions should be responsible for proper packaging (easy way to
install the software and its dependencies, together with startup scripts
and other system integration), and would be responsible for more general
bugfix updates that match their maintenance policy.

With such a split, you obviously *will* end up with a subpar user
experience if you try to manually install the software from the released
code. But you facilitate packaging, so you should end up being packaged
in more distributions. I think time is better spent contacting
distributions to get packaged rather than trying to improve the manual
installation to the point where it is actually usable.

### Freshness

One case where you end up doing manual installations (even on supported
distributions) is to get the latest released code running on
already-released distributions. Due to stable release policies in
distributions, they will release bugfix updates for the version that was
available when they released, but usually won't provide a whole new
version of a package.

The solution is in specific distribution archives that track the latest
upstream releases (like PPAs in Ubuntu) and make them available for
users of ﻿already-released distributions. Those are usually
co-maintained between distributions and upstream projects.

### Reference distributions

At this point, it is worth taking collaboration one step further, and
have developers that are involved in both projects ! Those can make sure
the distribution includes the packages and patches you need for your
software to run properly. Those can make sure the distribution is one on
which your software is up-to-date, runs properly and gets appropriate
bugfix updates. Those can maintain the ﻿specific distribution archives
for the latest upstream releases.

That distribution can then become a *reference distribution* for the
upstream project, one that is tightly integrated with the upstream
project and lives in harmony.

Two closing remarks:

-   You can have multiple reference distributions. That said, one way to
    limit friction and increase freshness is to have
    somewhat-synchronized release cycles, which may not scale very well.
-   I realize the proposed role split and reference distro scheme might
    not be generally applicable to all open source upstream projects. In
    my experience it worked well with server software.

In OpenStack, having a few Ubuntu core developers in the project (and
the Ubuntu server team supporting us) allows us to use Ubuntu as a
reference distribution. We have packages up for other distributions, but
those are not (yet) official distribution packages. Any other distro
developers interested to join ?

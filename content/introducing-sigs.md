Title: Introducing OpenStack SIGs
Date: 2017-08-10 14:12
Author: Thierry Carrez
Tags: OpenStack
Slug: introducing-sigs

Back in March in Boston, the OpenStack Board of Directors, Technical Committee,
User Committee and Foundation staff members met for a strategic workshop. The
goal of the workshop was to come up with a list of key issues needing attention
from OpenStack leadership. One of the strategic areas that emerged from that
workshop is the need to improve the feedback loop between users and developers
of the software. Melvin Hillsman volunteered to lead that area.

### Why SIGs ?

OpenStack was quite successful in raising an organized, vocal, and engaged
user community. However the developer and user communities are still mostly
acting as separate communities. Improving the feedback loop starts with
putting everyone caring about the same problem space in the same rooms and
work groups. The Forum (removing the artificial line between the Design Summit
and the Ops Summit) was a first step in that direction. SIGs are another step
in addressing that problem.

Currently in OpenStack we have various forms of workgroups, all attached to
a specific OpenStack governance body: User Committee workgroups (like the
Scientific WG or the Large Deployment WG), upstream workgroups (like the API
WG or the Deployment WG), or Board workgroups. Some of those are very focused
on a specific segment of the community, so it makes sense to attach them to a
specific governance body. But most are just a group of humans interested in
tackling a specific problem space together, and establishing those groups in
a specific community corner sends the wrong message and discourages
participation from everyone in the community.

As a result (and despite our efforts to communicate that everyone is welcome),
most TC-governed workgroups lack operator participants, and most UC-governed
workgroups lack developer participants. It's clearly not because the scope
of the group is one-sided (developers are interested in scaling issues,
operators are interested in deployment issues). It's because developers
assume that a user committee workgroup about "large deployments" is meant
to gather operator feedback rather than implementing solutions. It's because
operators assume that an upstream-born workgroup about "deployment" is only
to explore development commonalities between the various deployment strategies.
Or they just fly below the other group's usual radar. SIGs are about breaking
the artificial barriers and making it clear(er) that workgroups are for
everyone, by disconnecting them from the governance domains and the useless
upstream/downstream division.

### SIGs in practice

SIGs are neither operator-focused nor developer-focused. They are open groups,
with documented guidance on how to get involved. They have a scope, a clear
description of the problem space they are working to address, or of the use
case they want to better support in OpenStack. Their membership includes
affected users that can discuss the pain points and the needs, as well as
development resources that can pool their efforts to achieve the groups goals.
Ideally everyone in the group straddles the artificial line between operators
and developers and identifies as a little of both.

In practice, SIGs are not really different from the various forms of workgroups
we already have. You can continue to use the same meetings, git repositories,
and group outputs that you used to have. To avoid systematic cross-posting
between the openstack-dev and the openstack-operators mailing-lists, SIG
discussions can use the new [openstack-sigs mailing-list](http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-sigs),
SIG members can take advantage of our various events ([PTG](https://www.openstack.org/ptg),
Ops meetups, Summits) to meet in person.

### Next steps

We are only getting started. So far we only have one SIG: the "Meta" SIG, to
discuss advancement of the SIG concept. Several existing workgroups have
expressed their willingness to become early adopters of the new concept, so
we'll have more soon. If your workgroup is interested in being branded as a
SIG, let Melvin or myself know, we'll guide you through the process (which at
this point only involves being listed on a
[wiki page](https://wiki.openstack.org/wiki/OpenStack_SIGs)). Over time we
expect SIGs to become the default: most community-specific workgroups would
become cross-community SIGs, and the remaining workgroups would become more
like subteams of their associated governance body.

And if you have early comments or ideas on SIGs, please join the Meta
discussion on the
[openstack-sigs mailing-list](http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-sigs),
(using the [meta] subject prefix)!

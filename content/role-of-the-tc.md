Title: What is the role of the OpenStack Technical Committee
Date: 2016-10-03 12:45
Author: Thierry Carrez
Tags: OpenStack
Slug: role-of-the-tc

This week we are [renewing 6 seats](http://governance.openstack.org/election/)
in the 13-member OpenStack Technical Committee. This election has attracted
a large number of candidates, which is a great sign that people care about
the Technical Committee. At the same time, there is a lot of misconceptions
in our community about what the TC is for, what it can or cannot do, and the
overlap with other groups. I'll try to clarify that in this post.

### A misleading name

Part of the reason why there are so many misconceptions about the role of the
TC is that its name is pretty misleading. The Technical Committee is not
primarily technical: most of the issues that the TC tackles are open source
project governance issues. The TC is not really a committee either: it is a
group of elected people who will vote on resolutions and changes that are
proposed and which affect OpenStack as a whole. In the US, it is closer to
the Supreme Court than to anything else.

The primary role of the TC is to act as the final decision stage when it comes
to decision-making in the OpenStack open source project. It is extremely
important in an open source project to have a "bucket stops here" body that is
empowered to make decisions for the project if consensus and agreement cannot
be reached elsewhere -- otherwise it risks complete stand-still. I have been
involved in projects which were stuck in such governance grey area, and it
is a pretty ugly situation. It's interesting to note that the mere existence
of the final decision-making body is enough to achieve consensus at the lower
levels: two teams will prefer to find agreement between themselves rather
than call for final arbitration by the TC. This is a feature, not a bug.

### An evolving mission

The mission of the TC is to lead the development of "OpenStack". As OpenStack
evolved into one framework with a lot of collaborating components, each of
which developed by project teams with their own governance, the mission of
the TC also evolved. Those days we focus on the "OpenStack" experience. What
does it mean to be an OpenStack project ? What does it imply in terms of
development practices, general principles, common goals, cooperation, minimal
QA or user experience ? Is this new group applying to become an official
OpenStack project team following enough of those rules to be considered "one
of us" ?

Some people would like the TC to single-handedly solve upgrades, scalability,
interoperability or end user experience. Some other people would like the
TC to let the individual project teams do as they want. Reality is, neither
of those extremes are likely to happen. The TC is just 13 (usually busy)
people, they can't solve all the issues in OpenStack by themselves. They are
elected because we trust them to make the right decisions for OpenStack, not
because they are the ultimate 100x engineers who can fix everything. On the
other hand, the TC is not powerless: by continuously refining what it means to
be an "OpenStack project", it can influence OpenStack project teams to address
the right topics. We did that through assert tags, which encouraged teams to
improve their upgrade story or adopt a sane feature deprecation policy. We'll
do that through release cycle goals, to drive visible improvements across
all the components in OpenStack.

### Help, please

This is also why the TC needs all the help it can get. I'm excited we now have
the [Architecture workgroup](https://wiki.openstack.org/wiki/Meetings/Arch-WG),
an open group of people interested in addressing long-standing architecture
issues in OpenStack as a whole. I'm thrilled that we have a
[Stewardship workgroup](https://wiki.openstack.org/wiki/Meetings/SWGMeeting),
an open group of people encouraging leaders in OpenStack to adopt Servant
Leadership practices and tools. We are electing 13 members to vote and make
the final calls, but all the ideas don't have to come from those 13 members.
If you're a candidate and you're not elected, it doesn't prevent you from
working on governance problems and propose changes.

So... If you are an eligible voter, please take the time to read the candidates
platform emails and vote. Whoever gets elected, they will need the legitimacy
that only a good turnout in elections can give them. And if you are a candidate
and don't get elected, please consider joining those open workgroups, and
propose governance changes -- keeping "OpenStack" together is definitely not
a 13-people task.

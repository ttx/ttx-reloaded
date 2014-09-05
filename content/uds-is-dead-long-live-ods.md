Title: UDS is dead, long live ODS
Date: 2013-03-04 16:44
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: uds-is-dead-long-live-ods

Back from a (almost) entirely-offline week vacation, a lot of news were
waiting for me. A [full
book](http://openstack.booktype.pro/openstack-operations-guide/_draft/_v/1.0/why-we-wrote-this-book/)
was written. OpenStack projects
[graduated](http://eavesdrop.openstack.org/meetings/tc/2013/tc.2013-02-26-20.03.html).
An Ubuntu [rolling release
model](https://lists.ubuntu.com/archives/ubuntu-devel/2013-February/036537.html)
was considered. But what grabbed my attention was the announcement of
[UDS moving to a virtual
event](https://lists.ubuntu.com/archives/ubuntu-devel/2013-February/036502.html).
And every 3 months. And over two days. And next week.

As someone who attended all UDSes (but one) since Prague in May 2008, as
a Canonical employee then as an upstream developer, that was quite a
shock. We all have fond memories and anecdotes of stuff that happened
during those Ubuntu developer summits.

### What those summits do

For those who never attended one, UDS (and the OpenStack *Design
Summits* that were modeled after them) achieve a lot of goals for a
community of open source developers:

1.  Celebrate recent release, motivate all your developer community for
    the next 6 months
2.  Brainstorm early ideas on complex topics, identify key stakeholders
    to include in further design discussion
3.  Present an implementation plan for a proposed feature and get
    feedback from the rest of the community before starting to work on
    it
4.  Reduce duplication of effort by getting everyone working on the same
    type of issues in the same room and around the same beers for a few
    days
5.  Meet in informal settings people you usually only interact with
    online, to get to know them and reduce friction that can build up
    after too many heated threads

This all sounds very valuable. So why did Canonical decide to suppress
UDSes as we knew them, while they were arguably part of their successful
community development model ?

### Who killed UDS

The reason is that UDS is a very costly event, and it was becoming more
and more useless. A lot of Ubuntu development happens within Canonical
those days, and UDS sessions gradually shifted from being brainstorming
sessions between equal community members to being a formal communication
of upcoming features/plans to gather immediate feedback (point [3]
above). There were not so many brainstorming design sessions anymore
(point [2] above, very difficult to do in a virtual setting), with
design happening more and more [behind Canonical
curtains](http://www.markshuttleworth.com/archives/1200). There is less
need to reduce duplication of effort (point [4] above), with less
non-Canonical people starting to implement new things.

Therefore it makes sense to replace it with a less-costly,
purely-virtual communication exercise that still perfectly fills point
[3], with the added benefits of running it more often (updating everyone
else on status more often), and improving accessibility for remote
participants. If you add to the mix a move to rolling releases, it
almost makes perfect sense. The problem is, they also get rid of points
[1] and [5]. This will result in a even less motivated developer
community, with more tension between Canonical employees and
non-Canonical community members.

I'm not convinced that's the right move. I for one will certainly regret
them. But I think I understand the move in light of Canonical's recent
strategy.

### What about OpenStack Design Summits ?

Some people have been asking me if OpenStack should move to a similar
model. My answer is *definitely not*.

When Rick Clark imported the UDS model from Ubuntu to OpenStack, it was
to fulfill one of the [4 Opens](https://wiki.openstack.org/wiki/Open) we
pledged: *Open Design*. In OpenStack Design Summits, we openly debate
how features should be designed, and empower the developers in the room
to make those design decisions. Point [2] above is therefore essential.
In OpenStack we also have a lot of different development groups working
in parallel, and making sure we don't duplicate effort is key to limit
friction and make the best use of our resources. So we can't just pass
on point [4]. With more than 200 different developers authoring changes
every month, the OpenStack development community is way past [Dunbar's
number](http://en.wikipedia.org/wiki/Dunbar%27s_number). Thread after
thread, some resentment can build up over time between opposed
developers. Get them to informally talk in person over a coffee or a
beer, and most issues will be settled. Point [5] therefore lets us keep
a healthy developer community. And finally, with about 20k changes
committed per year, OpenStack developers are pretty busy. Having a week
to celebrate and recharge motivation batteries every 6 months doesn't
sound like a bad thing. So we'd like to keep point [1].

So for OpenStack it definitely makes sense to keep our Design Summits
the way they are. Running them as a track within the OpenStack Summit
allows us to fund them, since there is so much momentum around OpenStack
and so many people interested in attending those. We need to keep
improving the remote participation options to include developers that
unfortunately cannot join us. We need to keep doing it in different
locations over the world to foster local participation. But meeting in
person every 6 months is an integral part of our success, and we'll keep
doing it.

Next stop is in Portland, from April 15 to April 18. [Join
us](http://www.openstack.org/summit/) !

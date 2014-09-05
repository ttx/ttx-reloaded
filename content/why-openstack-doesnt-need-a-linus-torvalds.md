Title: Why OpenStack doesn't need a Linus
Date: 2012-10-25 12:46
Author: Thierry Carrez
Tags: Open source, OpenStack, Popular
Slug: why-openstack-doesnt-need-a-linus

As comparing OpenStack with Linux becomes an [increasingly popular
exercise](http://www.devx.com/blog/is-openstack-the-linux-of-cloud.html),
it's only natural that people and press articles start to ask where the
Linus Torvalds of OpenStack is, or [who the Linus Torvalds of
OpenStack](http://www.networkworld.com/news/2012/102412-openstack-linus-263659.html?hpg1=bn)
should be. This assumes that technical leaders could somehow be
appointed in OpenStack. This assumes that the single dictator model is
somehow reproducible or even desirable. And this assumes that the
current technical leadership in OpenStack is somehow lacking. I think
all those three assumptions are wrong.

Like Linux, OpenStack is an Open Innovation project: an independent,
common technical playground that is not owned by a single company and
where contributors form a meritocracy. Assuming you can somehow appoint
leaders in such a setting shows a great ignorance of how those projects
actually work. Leaders in an open innovation project don't derive their
authority from their title. They derive their authority from the respect
that the other contributors have for them. If they lose this respect,
their leadership will be disputed and you'll face the risk of a fork.
**Project leaders are not appointed, they are grown.** Linus wasn't
appointed, and he didn't decide one day that he should lead Linux. He
grew as the natural leader for this community over time.

Maybe people asking for a Linus of OpenStack like the idea of a single
dictator sitting at the top. But that setup is **not easily
reproduced**. Three conditions need to be met: you have to be the
founder (or first developer) of the project, your project has to grow
sufficiently slowly so that you can gather the undisputed respect of
incoming new contributors, and you have to keep your hands deep in
technical matters over time (to retain that respect). Linus checked all
those boxes. In OpenStack, there were a number of developers involved in
it from the start, and the project grew really fast, so a group of
leaders emerged, rather than a single undisputed figure.

I'd also argue that the "single leader" model is **not really
desirable**. OpenStack is not a single project, it's a collection of
projects. It's difficult to find a respected expert in all areas,
especially as we grew by including new projects within the OpenStack
collection. In addition to that, Linux as a project still struggles with
its [bus factor](http://en.wikipedia.org/wiki/Bus_factor) of 1 and how
it would survive Linus. Organizing your technical leadership in a way
that makes it easier for leadership to transition to new figures makes a
stronger and more durable community.

Finally, asking for a Linus of OpenStack is somehow implying that the
current technical leadership is insufficient, which is at best ignorant,
at worse insulting. Linus fills two roles within Linux: the *technical
lead* role (final decision on technical matters, the buck stops here)
and the *release management* role (coordinating the release development
cycles and producing releases). OpenStack has project technical leads
("PTLs") to fill the first role, and a (separate) release manager to
fill the second. In addition to that, to solve cross-project issues, we
have a [Technical
Committee](https://www.openstack.org/foundation/technical-committee/)
(which happens to include the PTLs and release manager).

If you are under the impression that this multi-headed technical
leadership might result in non-opiniated choices, think twice. The new
governance model establishing the Technical Committee and the full
authority of it over all technical matters in OpenStack is only a month
old, previously the project (and its governance model) was still owned
by a single company. The PTLs and Technical Committee members are highly
independent and have the interests of the OpenStack project as their top
priority. Most of them actually changed employers over the last year and
continued to work on the project.

I think what the press and the pundits actually want is a more visible
public figure, that would make stronger design choices, if possible with
nice punch lines that would make [good
quotes](http://en.wikiquote.org/wiki/Linus_Torvalds). It's true that the
explosive growth of the project did not leave a lot of time so far for
technical leaders of OpenStack to engage with the press. It's true that
the OpenStack leadership tends to use friendly words and prefer
consensus where possible, which may not result in memorable quotes. But
confusing that with weakness is really a mistake. Technical leadership
in OpenStack is just fine the way it is, thank you for asking.

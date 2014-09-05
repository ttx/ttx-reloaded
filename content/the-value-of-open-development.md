Title: The value of Open Development
Date: 2012-10-23 15:57
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: the-value-of-open-development

Mark's recent blogpost on [Raring community
skunkworks](http://www.markshuttleworth.com/archives/1200) got me
thinking. I agree it would be unfair to spin this story as
Canonical/Ubuntu switching to closed development. I also agree that (as
the damage control messaging was [quick to point
out](http://www.markshuttleworth.com/archives/1207)) inviting some
members of the community to participate in closed development projects
is actually a step towards more openness rather than a step backwards.

That said, it certainly is making the "closed development" option more
official and organized, which is not a step in the right direction in my
opinion. It reinforces it as a perfectly valid option, while I would
really like it to be an exception for corner cases. So at this point, it
may be useful to insist a bit on the benefits of open development, and
why dropping them might not be that good of an idea.

*Open Development* is a transparent way of developing software, where
source code, bugs, patches, code reviews, design discussions, meetings
happen in the open and are accessible by everyone. "Open Source" is a
prerequisite of open development, but you can certainly do open source
without doing open development: that's what I call *the Android model*
and what others call *Open behind walls* model. You can go further than
open development by also doing "Open Design": letting an open community
of equals discuss and define the future features your project will
implement, rather than restricting that privilege to a closed group of
"core developers".

Open Development allows you to "release early, release often" and get
the testing, QA, feedback of (all) your users. This is actually a good
thing, not a bad thing. That feedback will help you catch corner cases,
consider issues that you didn't predict, get outside patches. More
importantly, Open Development helps lowering the *barrier of entry* for
contributors to your project. It blurs the line between consumers and
producers of the software (no more "*us* vs. *them*" mentality),
resulting in a much more engaged community. Inviting select individuals
to have early access to features before they are unveiled sounds more
like a proprietary model beta testing program to me. It won't give you
the amount of direct feedback and variety of contributors that open
development gives you. Is the trade-off worth it ?

How much as I dislike the Android model, I understand that the ability
for Google to give *some* select OEMs a bit of advance has *some* value.
Reading Mark's post though, it seems that the main benefits for Ubuntu
are in avoiding early exposure of immature code and get more splash PR
effect at release time. I personally think that short-term, the drop in
QA due to reduced feedback will offset those benefits, and long-term,
the resulting drop in community engagement will also make this a bad
trade-off.

In OpenStack, we founded the project on [the Four
Opens](http://wiki.openstack.org/Open): Open Source, Open Development,
Open Design and Open Community. This early decision is what made
OpenStack so successful as a community, not the "cloud" hype. Open
Development made us very friendly to new developers wanting to
participate, and once they experienced Open Design (as exemplified in
our Design Summits) they were sold and turned into advocates of our
model and our project within their employing companies. Open Development
was really instrumental to OpenStack growth and adoption.

In summary, I think Open Development is good because you end up
producing better software with a larger and more engaged community of
contributors, and if you want to drop that advantage, you better have a
very good reason.

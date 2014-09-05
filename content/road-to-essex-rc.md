Title: The road to OpenStack Essex release candidates
Date: 2012-03-16 12:57
Author: Thierry Carrez
Tags: OpenStack
Slug: road-to-essex-rc

Since the beginning of March, OpenStack developers are focusing on
testing and bugfixes, with the objective of producing a release
candidate for each project.

Regular readers of my blog know I'm not the last one to complain when I
feel developers don't care about the release and don't participate to
that critical sequence of the cycle. I'm happy to report that the
engagement of developers around making Essex good is overwhelming.
Driven by technical leads that understand the challenges, significant
groups of old and new developers are participating, testing, assigning
themselves to bugs reported by others and fixing them in record time. As
project-focused groups, I think we are quickly maturing.

So, how far are we from Essex today ? The final release is set to April
5th, which means each core project needs to produce its final release
candidate before then. As of today no project did produce a release
candidate yet.

Swift is expected to release its final Essex version (1.4.8) on March
22. This version will be included in OpenStack Essex release, unless a
critical regression is detected in it.

Keystone (which every other project depends on) is still struggling with
9 RC bugs, including some key decisions to be made on configuration
handling. This is the hot spot right now: if you have free cycles,
please consider asking Joe Heck (heckj on IRC) how you can best help the
Keystone crew. I'd really like to have an RC1 for that project by
Thursday next week.

Glance also looks still a bit far away, with 5 RC bugs listed and slow
progress on them. I still hope Glance can be ready by Tuesday next week
though.

Nova is looking quite good, with 2 RC bugs left on the list. The trick
with Nova is that regressions and critical issues can hide in dark
corners of its 120k lines of code, so the focus is really on finding the
remaining issues, filing and targeting them. I expect we'll be able to
publish RC1 on Monday or Tuesday next week.

Horizon is almost ready (3 RC bugs left), waiting for a few fixes to
land in other projects before it can issue its RC1. It should be out
early next week.

Once all projects release their RC1, the hunt for the overlooked
release-critical issue will be on. It will be time to put the proposed
release to the test. In order to limit potential last-minute
regressions, only showstoppers will warrant a respin of the release
candidate, other bugs will be listed in the Known Bugs section of the
release notes. You can use the "essex-rc-potential" tag to mark bugs
that you think should be fixed before we release Essex.

Let's all make it rock !

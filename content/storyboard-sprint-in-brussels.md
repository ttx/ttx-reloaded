Title: StoryBoard sprint in Brussels
Date: 2014-02-05 15:20
Author: Thierry Carrez
Tags: OpenStack
Slug: storyboard-sprint-in-brussels

StoryBoard is a project I started a few months ago. We have been running
into a number of issues with Launchpad (inability to have blueprints
spanning multiple code bases, inability to have flexible project group
views, inability to use non-Launchpad OpenID for login...), and were
investigating replacements. I was tired to explain why those
alternatives wouldn't work for our task tracking, so I started to
describe the features we needed, and ended up writing a proof-of-concept
to show a practical example.

![storyboard-poc]({filename}/images/storyboard-old.png)

That proof-of-concept was sufficiently compelling that the
Infrastructure team decided we should follow the path of writing our own
tool. To be useful, task tracking for complex projects has to precisely
match your workflow. And the POC proved that it wasn't particularly
difficult to write. Then people from HP, Mirantis and RedHat joined this
effort.

My Django-based proof-of-concept had a definite last-century feel to it,
though. We wanted a complete REST API to cover automation and scripting
needs, and multiple clients on top of that. Time was ripe for doing
things properly and start building a team effort around this. Time was
ripe for... the StoryBoard sprint.

We gathered in Brussels for two days in advance of FOSDEM, in a meeting
room sponsored by the OpenStack Foundation (thanks!). On day 2 we were
12 people in the room, which was more than we expected !

![sprint]({filename}/images/storyboard-sprint.jpg)

Colette helped us craft a mission statement and structure our goals.
Michael presented an architecture (static JS client on top of
OpenStack-like REST service) that we blessed. Jaromir started to draw
wireframes. Sergey, Ruslan and Nikita fought uncooperative consulates
and traveled at night to be present on day 2. We also confirmed a number
of other technology choices (Bootstrap, AngularJS...). We discussed the
basic model, bikeshedded over StoryBoard vs. Storyboard and service
URLs. We got a lot covered, had very few breaks, ate nice food and drank
nice beer. But more importantly, we built a strong set of shared
understandings which should help us make progress as a united team going
forward.

We have automated testing and continuous deployment set up now, and once
the initial basic functionality is up (MVP0) we should iterate fast. The
Infrastructure program is expected to be the first to dogfood this, and
the goal is to have something interesting to present to other programs
by the Atlanta summit. To participate or learn more about StoryBoard,
please join us on \#storyboard on Freenode IRC, or at our [weekly
meeting](https://wiki.openstack.org/wiki/Meetings#StoryBoard_Meeting).

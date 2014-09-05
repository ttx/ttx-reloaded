Title: Ask not what OpenStack can do for you...
Date: 2012-04-04 12:09
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: ask-not-what-openstack-can-do-for-you

Over the last months I've seen more and more tweets and news articles
using the formulation "OpenStack should", as in "OpenStack should
support Amazon APIs since it's the de-facto standard". I think there is
a fundamental misconception there and I'd like to address it.

As a quick aside (and contrary to what the twittersphere sometimes
report), it should be noted that OpenStack Nova always supported the
Amazon EC2 API, and that OpenStack Swift grew an Amazon S3 compatibility
layer last year. That said, I'll be the first to admit that one could
rightfully claim that the AWS API support in OpenStack is in less better
shape than the OpenStack API support. But the reason behind it is not
some "OpenStack strategy", it's a reflection of the participating
companies focus.

OpenStack is a true *Open Innovation* project. It's a collaboration
ground where multiple companies are free to invest development resources
to care about the stuff that is important to them. It's an influence
game where you need to donate developers to play: OpenStack is the
playing field, not the players that push the ball.

Red Hat cared about QPID support, they fielded developers to make it
happen in OpenStack. EC2 API support is originally in Nova because NASA
cared about it. Then with the increase of Rackspace's influence on the
project, the OpenStack API grew faster. Now with Canonical (and others)
interest, Amazon's API support is getting better. Ultimately, code
talks, and you can make things happen. That's what makes OpenStack so
appealing but also so confusing to the industry.

As "OpenStack", we need to make sure the playing field is level (and
hopefully the Foundation will be set up soon enough to address that) and
that the code is modular and welcoming. But it's up to the participating
companies, which throw development resources at the project, to invest
in what's important for them or their customers. And maintain it over
the long run.

So whenever you say "OpenStack should", ask yourself if you shouldn't
really be saying... [Rackspace, Cisco, HP, IBM, Red Hat...] should. Ask
not what OpenStack can do for you. Ask what you can do for OpenStack.

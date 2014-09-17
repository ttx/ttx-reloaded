Title: The next steps for Zaqar
Date: 2014-09-17 15:00
Author: Thierry Carrez
Tags: OpenStack
Slug: next-steps-for-zaqar

Yesterday the
[OpenStack Technical Committee](https://wiki.openstack.org/wiki/Governance/TechnicalCommittee)
concluded the end-of-cycle graduation review for
[Zaqar](https://wiki.openstack.org/wiki/Zaqar)
(the project previously called Marconi), and decided Zaqar should stay in
incubation during the Kilo cycle.

## What it does not mean

It does not mean that the Zaqar developers failed to deliver. The Zaqar team
crossed all the checkboxes in our
[integration requirements](http://git.openstack.org/cgit/openstack/governance/tree/reference/incubation-integration-requirements.rst)
checklist. They consistently took into account our feedback and proved
themselves ready to make any required change. This is why the decision appears
so unfair to them: they could not really do more.

It does not mean that OpenStack wouldn't benefit from a basic queue/messaging
service. If anything, it means that we actually care a lot about such a
service, enough to have strong opinions about how it should be done, the scope
of the designed solution and what exact use cases it enables or prevents.

## What it does mean

It does mean that our incubation process is broken. The Technical Committee
could not provide to the Zaqar team the feedback they needed to be successful.
It could not discuss Zaqar's scope and design well before the end-of-cycle
graduation review, when time constraints push for a quick decision. In this
cycle the TC focused on existing issues with existing integrated projects (like
the Neutron/nova-network gaps), which some might argue need to be fixed before
we add more integrated projects. We ended up not having the time to follow up
on incubated projects as much as we should have.

The good news here is that the gap coverage for existing integrated projects
during the Juno cycle was generally successful, so this was probably more of a
one-time thing. If we preserve the incubation process as-is, next cycle we plan
to assign a specific TC member mentor to every incubated project, so that we
provide consistent feedback and raise the necessary discussions in due time.

It does also mean that our "in or out" integrated release model is broken.
Having a single class you can graduate to means accepting a new integrated
project has a significant cost on existing horizontal teams. The integrated
release is therefore very conservative -- if there is any doubt, better leave
the incubated project to resolve those doubts while in incubation, rather than
in the first integrated cycle with the time pressure of the next release date.
And if it's not "in", it's just "out". There is no intermediary area. If we had
several classes (or layers), triggering different amounts of resources, then it
would be much less black or white and we could have a conservative class and an
inclusive class. We are just starting a discussion at the TC level on how we
could evolve that model (and the "programs" that back that model) to allow us
to scale.

## The next steps

What's up next for Zaqar, then ? It is the duty of the Technical Committee to
explain its decision, and work out under which conditions it would accept Zaqar
in 6 months time. So now that we are free from the time pressure of the
integration decision, we need to determine which options are on the table and
which ones would be preferred. This should happen in the coming weeks, before
the Design Summit in Paris. Then we really need to follow-up on that feedback,
by designating a member from the newly-elected TC as the Zaqar mentor, tasked
with making sure the communication lines stay open at all times and we stay in
alignment. We need to learn from our mistakes, and not find ourselves in the
same position in 6 months.

Finally, depending on the outcome of the integrated release model evolution
discussion, it is possible that the decision to stay in incubation during the
Kilo cycle will not matter that much. If we set up a layered model for example,
it is very possible that Zaqar would directly appear on that map. So my advice
would be to follow closely how that discussion goes to see how it may affect
Zaqar in the near future.

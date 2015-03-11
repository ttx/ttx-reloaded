Title: Stepping out of the way
Date: 2015-03-11 17:45
Author: Thierry Carrez
Tags: OpenStack
Slug: stepping-out-of-the-way

In the early days of OpenStack, we instituted a do-acracy: power to people
that do things over people that don't. Code talks: when unsure on the direction
to go, the one that came with code basically won. Don't ask for permission,
ask for forgiveness. Make progress, fix issues if they arise. That let us
positively move forward fast in the early days.

After some time, our community realized this didn't necessarily scale, and
this didn't necessarily result in quality. As we kept on adding contributors
way beyond our initial trusted small circle, we couldn't rely solely on our
common culture and shared understandings anymore. We started introducing
safeguards, the most visible and successful one being our code gating system
(which relies on human code reviews and automated tests to prevent unacceptable
code from merging). We started writing down our rules and governance, since
our ever-increasing group couldn't rely on oral tradition and shared experience
anymore. As picky newcomers complained about governance rules holes in every
gray area, we started defining the process to define process.

I think we struck the right balance on those days between allowing our
community to grow and letting people do things. But the movement to add rules
unfortunately didn't stop then, it continues today. We added specs, which if
used with moderation (like only for significant features) are a great way to
avoid wasted development effort, but used blindly are a great way to increase
the length of our feature development pipeline and increase frustration. We
added automated tests to verify the presence (or is it absence ?) of a
trailing dot in commit message titles. We started to get in the way of getting
things done.

At the Technical Committee level, that translates into hours lost
rubberstamping stuff, hours we don't spend asking ourselves the right
questions (like: what is broken in OpenStack today and how to fix it). Do we
really need to approve a project team decision to add a new git repository ?
Or should we just let them do things, and consider reverting that action if it
ends up causing a problem ? It is an interesting balance to strike between
letting people go wild and approving their every move. On one side you don't
want them to waste energy on something you might end up striking down, but on
another side you don't want to block them when they first set out to create
stuff.

As of today, I think we pushed the regulation and "ask for permission" cursor
so far we actually prevent things from happening. I'd like us to step out of
the way. When a proposal is not perfect, I'd like us to propose a subsequent
patchset instead of blocking the review forever. At the Technical Committee
level, I'd like us to let people do more things, and retreat to being an
appeals board in case problems end up arising. The Technical Committee always
has been the ultimate appeals board in case problems can't find a resolution
at lower levels of our community. In practice, the mere existence of that
appeals board encouraged conflict resolution at lower levels, to the point
where I can't remember us being called to resolve an actual dispute. I'd like
our community to be more trusted by default, to ask more for forgiveness and
less for permission.

Trust is a weird thing. When your behavior is constrained by rules and
automated tooling, you tend to try to game the system and get the most you
can of it. But when trust is placed on you to do the right thing, the
incentive is to avoid abusing the trust that is placed on you, to prove
yourself worthy of that trust.

So I'd like us (our community in general and the Technical Committee in
particular) to look into our processes and see where we can remove ourselves
from the action pipeline. Where we can trust by default and rely on our
escalation mechanisms to resolve issues as they arise (if they arise). That
may come out as weird coming from a process/governance wonk like me, but that
is my new motto for the Liberty cycle: "step out of the way".


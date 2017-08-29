Title: What to expect from the Queens PTG
Date: 2017-08-29 12:02
Author: Thierry Carrez
Tags: OpenStack
Slug: queens-ptg

In less than two weeks, OpenStack upstream developers and project team members
will assemble in Denver, Colorado for a week of team discussions, kickstarting
the [Queens development cycle](https://releases.openstack.org/queens/schedule.html).

Attending [the PTG](https://www.openstack.org/ptg) is a great way to make
upstream developers more efficient and productive: participating in the new
development cycle organization, solving early blockers and long-standing
issues in-person, and building personal relationships to ease interactions
afterwards.


## What changed since Atlanta ?

The main piece of feedback we received from the Pike PTG in Atlanta was that
with the ad-hoc discussions and dynamic scheduling, it was hard to discover
what was being discussed in every room. This was especially an issue during
the first two days, where lots of vertical team members were around but did
not know which room to go to.

In order to address that issue while keeping the scheduling flexibility that
makes this event so productive, we created an IRC-driven dynamic notification
system. Each room moderator is able to signal what is being discussed right
now, and what will be discussed next in the `#openstack-ptg` IRC channel. That
input is then collected into a mobile-friendly webpage for easy access. That
page also shows sessions scheduled in the reservable extra rooms via Ethercalc,
so it's a one-stop view of what's being currently discussed in every room,
and what you could be interested in joining next.

The other piece of feedback that we received in Atlanta was that the
horizontal/vertical week slicing was suboptimal. Having all horizontal teams
(QA, Infra, Docs) meet on Monday-Tuesday and all vertical teams (Nova, Cinder,
Swift) meet on Wednesday-Friday was a bit arbitrary and did not make an optimal
use of the time available.

For Denver we still split the week in two, but with a slightly different
pattern. On Monday-Tuesday we'll have inter-team discussions, with rooms
centered more on topics than on teams, focused on solving problems.
On Wednesday-Friday we'll have intra-team discussions, focused on organizing,
prioritizing and bootstrapping the work for the rest of the deployment cycle.
Such a week split won't magically suppress all conflicts obviously, but we
hope it will improve the overall attendee experience.


## What rooms/topics will we have on Monday-Tuesday ?

**Compute stack / VM & BM WG (#compute)**:
In this room, we’ll have discussions to solve inter-project issues within the base compute stack (Keystone, Cinder, Neutron, Nova, Glance, Ironic…).

**API SIG (#api)**:
In this room, we’ll discuss API guidelines to further improve the coherence and compatibility of the APIs we present to the cloud user. Members of the SIG will also be hosting guided reviews of potential API changes, see the openstack-dev mailing list for more details.

**Infra / QA / RelMgt / Stable / Requirements helproom (#infra)**:
Join this room if you have any questions about or need help with anything related to the development infrastructure, in a large sense. Can be questions around project infrastructure configuration, test jobs (including taking advantage of the new Zuul v3 features), the “Split Tempest plugins” Queens goal, release management, stable branches, global requirements.

**Packaging WG (#packaging)**:
In this room, we’ll discuss convergence and commonality across the various ways to deploy OpenStack: Kolla, TripleO, OpenStackAnsible, Puppet-OpenStack, OpenStack Chef, Charms...

**Technical Committee / Stewardship WG (#tc)**:
In this room, we’ll discuss project governance issues in general, and stewardship challenges in particular.

**Skip-level upgrading (#upgrading)**:

Support for skip-level upgrading across all OpenStack components will be discussed In this room. We’ll also discuss increasing the number of projects that support rolling upgrades, zero-downtime upgrades and zero-impact upgrades.

**GUI helproom / Horizon (#horizon)**:
Join this room if you have questions or need help writing a Horizon dashboard for your project, and want to learn about the latest Horizon features. Horizon team members will also discuss Queens cycle improvements here.

**Oslo common libraries (#oslo)**:
Current and potential future Oslo libraries will be discussed in this room. Come to discuss pain points or missing features, or to learn about libraries you should probably be using.

**Docs / I18n helproom (#docs-i18n)**:
Documentation has gone through a major transition at the end of Pike, with more doc maintenance work in the hands of each project team. The Docs and I18n teams will meet in this room and be available to mentor and give guidance to Doc owners in every team.

**Simplification (#simplification)**:
Complexity is often cited as the #1 issue in OpenStack. It is however possible to reduce overall complexity, by removing unused features, or deleting useless configuration options. If you’re generally interested in making OpenStack simpler, join this room!

**Make components reusable for adjacent techs (#reusability)**:
We see more and more OpenStack components being reused in open infrastructure stacks built around adjacent technology. In this room we’ll tackle how to improve this component reusability, as well as look into things in adjacent communities we could take advantage of.

**CLI / SDK helproom / OpenStackClient (#cli)**:
In this helproom we’ll look at streamlining our client-side face. Expect discussions around OpenStackClient, Shade and other SDKs.

**"Policy in code" goal helproom (#policy-in-code)**:
For the Queens cycle we selected “Policy in code” as a cross-project release goal. Some teams will need help and guidance to complete that goal: this room is available to help you explain and make progress on it.

**Interoperability / Interop WG / Refstack (#interop)**:
Interoperability between clouds is a key distinguishing feature of OpenStack clouds. The Interop WG will lead discussions around that critical aspect in this room.

**User Committee / Product WG (#uc)**:
The User Committee and its associated subteams and workgroups will be present at the PTG too, with a goal all week to close the feedback loop from operators back to developers. This work will be prepared in this room on the first two days of the event.

**Security (#security)**:
Security is a process which requires continuous attention. Security-minded folks will gather into this room to further advance key security functionality across all OpenStack components.


## Which teams are going to meet on Wednesday-Friday ?

The following project teams will meet for all three days:
**Nova**, **Neutron**, **Cinder**, **TripleO**, **Ironic**, **Kolla**,
**Swift**, **Keystone**, **OpenStack-Ansible**, **Infrastructure**, **QA**,
**Octavia**, and **Glance**.

The following project teams plan to only meet for two days, Wednesday-Thursday:
**Heat**, **Watcher**, **OpenStack Charms**, **Trove**, **Congress**,
**Barbican**, **Mistral**, **Freezer**, **Sahara**, **Glare**, and
**Puppet OpenStack**.

## Join us!

We already have more than 360 people signed up, but we still have room for you!
[Join us](https://www.eventbrite.com/e/project-teams-gathering-denver-2017-tickets-33219389087) if you can. The ticket price will increase this Friday though,
so if you plan to register I'd advise you to do so ASAP to avoid the
last-minute price hike.

The event hotel is pretty full at this point (with the last rooms available
priced accordingly), but there are
[lots of other options](http://lists.openstack.org/pipermail/openstack-dev/2017-August/121192.html)
nearby.

See you there!


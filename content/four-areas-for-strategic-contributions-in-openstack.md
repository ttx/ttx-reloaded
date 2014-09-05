Title: Four areas for strategic contributions in OpenStack
Date: 2011-10-06 18:46
Author: Thierry Carrez
Tags: OpenStack
Slug: four-areas-for-strategic-contributions-in-openstack

The OpenStack Essex Design Summit just ended, and several people those
last three days have asked me to give a bit more substance to what I
exactly meant by "Strategic contributions" in my [last
article]({filename}/the-next-step-for-openstack.md).
Ensure the long-term health of the project by investing in
project-centered resources, right, but what can we do now ? What actions
can we take today ?

Based on the very interesting Summit discussions we had, I think the
strategic contributions that can be made today fall into 4 categories.

### Commonality

Brian Lamar had a great session on reviving the OpenStack Common effort:
identifying common functions between OpenStack projects, converge
towards the same implementation, and maintain it in a common library.
The goal is double: present a more uniform face (logs and configuration
files, for example, should follow the same syntax), and make sure that
we don't waste precious development resources on useless duplicate
works. This effort failed in the past due to lack of resources being
dedicated long-term to it, so it sounds like a nice and easy area to
start contributing strategically.

### Consistency

The second (and related) area is consistency. Tactical contributions
have advanced the state of very specific features applying to very
specific setups, at the expense of the resulting coherence. Vish lead a
good session on making the featureset between KVM and Xen hypervisors
converge, not only in terms of functions, but also in term of concepts.
I think that analysis needs to happen more generally in OpenStack: is
the resulting product coherent ? How can we plug the holes in those
feature matrixes ?

### Security

Another important area that emerged from the Summit, especially with Ray
Hookway's session, is work on security. Strengthen the architecture (to
limit the attack surface and lay defense in depth), formalize the
process around vulnerablity handling and disclosure, and coordinate the
necessary effort on auditing. This work is just getting started, and I
hope I will find time to help setting it up.

### Quality

Last but certainly not least, we need to invest in durable quality. Jay
Pipes pushed a number of sessions where we pinpointed the need to
identify the issues (QA), fix them (Bug squads) and prevent them from
happening again (automated tests & continuous integration). That's by
far the most complex area and the most difficult to coordinate, but the
basic resource needed there is manpower, and the setup of
company-neutral common workgroups that everyone can contribute to is the
first step.

Whether you bet your business on OpenStack, or you're just interested in
the long-term health of the open source project, give your developers
time to contribute to those areas and workgroups, and we'll all be a lot
better as a result.

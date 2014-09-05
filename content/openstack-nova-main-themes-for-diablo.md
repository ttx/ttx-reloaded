Title: OpenStack Nova: Main themes for Diablo
Date: 2011-05-20 12:47
Author: Thierry Carrez
Tags: OpenStack
Slug: openstack-nova-main-themes-for-diablo

A few weeks after the OpenStack Design Summit in Santa Clara, we are
starting to get a better picture of [what should
be](https://blueprints.launchpad.net/nova/diablo) in the next version of
OpenStack Nova, codenamed *Diablo*, [scheduled for
release](http://wiki.openstack.org/DiabloReleaseSchedule) on September
22.

One big priority of this release is to [separate
code](https://blueprints.launchpad.net/nova/+spec/separate-code-for-services)
for the network and volume services, and [refactor nova-network
code](https://blueprints.launchpad.net/nova/+spec/network-refactoring)
to add a [clear internal
API](https://blueprints.launchpad.net/nova/+spec/implement-network-api).
This will allow to plug separate
[network](https://blueprints.launchpad.net/nova/+spec/integrate-network-services)
and
[volume](https://blueprints.launchpad.net/nova/+spec/integrate-block-storage)
service providers, and pave the way for integration with future
OpenStack projects like
[Quantum/Melange/Donabe](https://launchpad.net/netstack) and
[LunR](https://launchpad.net/lunr). In preparation for this, we'll push
changes to [rely more on the
queue](https://blueprints.launchpad.net/nova/+spec/no-db-messaging) (and
less on the database) to pass information between components. In the
same area, we need some more changes to [support multiple
NICs](https://blueprints.launchpad.net/nova/+spec/nova-multi-nic) and
should also provide a client OpenStack API for directly [interacting
with
volumes](https://blueprints.launchpad.net/nova/+spec/implement-volume-api).

A second theme of the Diablo release is the new [distributed
scheduler](https://blueprints.launchpad.net/nova/+spec/distributed-scheduler),
which should be able to schedule across zones and taking capabilities
into account. This will need changes in the way we [reference
instances](https://blueprints.launchpad.net/nova/+spec/nova-instance-referencing),
as well as some changes for [EC2 API
compatibility](https://blueprints.launchpad.net/nova/+spec/ec2-id-compatibilty).

On the API side, we should [finalize OpenStack API
1.1](https://blueprints.launchpad.net/nova/+spec/openstack-compute-api-11-finalization)
support, including work on [floating
IPs](https://blueprints.launchpad.net/nova/+spec/openstack-api-floating-ips)
and [shared IP
groups](https://blueprints.launchpad.net/nova/+spec/shared-ip-groups).
For administrators, [instance
migration](https://blueprints.launchpad.net/nova/+spec/instance-migration)
and [account administration
actions](https://blueprints.launchpad.net/nova/+spec/admin-account-actions)
should be added. We'll also ensure good AWS API
[compatibility](https://blueprints.launchpad.net/nova/+spec/reasonable-aws-compatibility)
and
[validation](https://blueprints.launchpad.net/nova/+spec/aws-api-validation).

Support for
[snapshotting](https://blueprints.launchpad.net/nova/+spec/snapshot-volume),
[cloning](https://blueprints.launchpad.net/nova/+spec/clone-volume) and
[booting](https://blueprints.launchpad.net/nova/+spec/boot-from-volume)
from volumes should land early in this cycle, as well as
[new](https://blueprints.launchpad.net/nova/+spec/configuration-drive)
[ways](https://blueprints.launchpad.net/nova/+spec/instance-transport)
of communicating configuration data between host and guest. We also need
to
[integrate](https://blueprints.launchpad.net/nova/+spec/integrate-nova-authn)
[with](https://blueprints.launchpad.net/nova/+spec/finalize-nova-auth)
AuthN/AuthZ with the new common Keystone authentication system. Lots of
other features are planned (and others might be added before the end),
you can check out the [blueprints
plan](https://blueprints.launchpad.net/nova/diablo) for more detail.

Last but not least, on the QA side, we should have [continuous automated
testing](https://blueprints.launchpad.net/nova/+spec/testing-jenkins-integration)
across a range of [reference
architectures](https://blueprints.launchpad.net/nova/+spec/reference-architectures)
and increase our [unittest and smoketest
coverage](https://blueprints.launchpad.net/nova/+spec/diablo-testing)
among
[other](https://blueprints.launchpad.net/nova/+spec/engineer-in-quality)
[efforts](https://blueprints.launchpad.net/nova/+spec/libvirt-refactoring)
[to](https://blueprints.launchpad.net/nova/+spec/nova-api-serialization)
build-in quality.

The first milestone for this cycle,
[diablo-1](https://launchpad.net/nova/+milestone/diablo-1), should be
released on June 2nd.

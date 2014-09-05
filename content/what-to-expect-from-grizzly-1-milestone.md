Title: What to expect from Grizzly-1 milestone
Date: 2012-11-23 14:14
Author: Thierry Carrez
Tags: OpenStack
Slug: what-to-expect-from-grizzly-1-milestone

The first milestone of the OpenStack Grizzly development cycle is [just
out](http://lists.openstack.org/pipermail/openstack-announce/2012-November/000054.html).
What should you expect from it ? What significant new features were
added ?

The first milestones in our [6-month development
cycles](http://wiki.openstack.org/ReleaseCycle) are traditionally not
very featureful. That's because we are just out of the previous release,
and still working heavily on bugs (this milestone packs 399 bugfixes !).
It's been only one month since we had our [Design
Summit](http://wiki.openstack.org/Summit), so by the time we formalize
its outcome into blueprints and roadmaps, we are just getting started
with feature implementation. Nevertheless, it collects a lot of new
features and bugfixes that landed in our master branches since
mid-September, when we froze features in preparation for the Folsom
release.

**Keystone** is arguably where the most significant changes landed, with
a [tech preview of the new API
version](https://blueprints.launchpad.net/keystone/+spec/implement-v3-core-api)
(v3), with [policy and RBAC
access](https://blueprints.launchpad.net/keystone/+spec/rbac-keystone-api)
enabled. A new [ActiveDirectory/LDAP identity
backend](https://blueprints.launchpad.net/keystone/+spec/ad-ldap-identity-backend)
was also introduced, while the auth\_token middleware is [now
shipped](https://blueprints.launchpad.net/keystone/+spec/authtoken-to-keystoneclient-repo)
with the Python Keystone client.

In addition to fixing [185
bugs](https://launchpad.net/nova/grizzly/grizzly-1), the **Nova** crew
[removed
nova-volume](https://blueprints.launchpad.net/nova/+spec/delete-nova-volume)
code entirely (code was kept in Folsom for compatibility reasons, but
was marked deprecated). Virtualization drivers [no longer directly
access the
database](https://blueprints.launchpad.net/nova/+spec/no-db-virt), as a
first step towards completely [isolating compute nodes from the
database](https://blueprints.launchpad.net/nova/+spec/no-db-compute).
Snapshots are now [supported on raw and LVM
disks](https://blueprints.launchpad.net/nova/+spec/snapshots-for-everyone),
in addition to qcow2. On the hypervisors side, the Hyper-V driver grew
[ConfigDrive v2
support](https://blueprints.launchpad.net/nova/+spec/hyper-v-config-drive-v2),
while the XenServer one can now [use
BitTorrent](https://blueprints.launchpad.net/nova/+spec/xenserver-bittorrent-images)as
an image delivery mechanism.

The **Glance** client is [no longer
copied](https://blueprints.launchpad.net/glance/+spec/separate-client)
within Glance server (you can still find it with the Python client
library), and the Glance [SimpleDB driver reaches feature
parity](https://blueprints.launchpad.net/glance/+spec/glance-simple-db-parity)
with the SQLAlchemy based one. A number of cleanups were implemented in
**Cinder**, including in [volume drivers code
layout](https://blueprints.launchpad.net/cinder/+spec/driver-cleanup)
and [API versioning
handling](https://blueprints.launchpad.net/cinder/+spec/cinder-apiv2). 
Support for [XenAPI storage manager for
NFS](https://blueprints.launchpad.net/cinder/+spec/xenapi-storage-manager-nfs)
is back, while the API grew a call to [list bootable
volumes](https://blueprints.launchpad.net/cinder/+spec/list-bootable-volumes)
and a [hosts
extension](https://blueprints.launchpad.net/cinder/+spec/cinder-hosts-extension)
to allow service status querying.

The **Quantum** crew was also quite busy. The [Ryu plugin was
updated](https://blueprints.launchpad.net/quantum/+spec/ryu-plugin-update-for-ryu)
and now features [tunnel
support](https://blueprints.launchpad.net/quantum/+spec/ryu-tunnel-support).
The preparatory work to [add advanced
services](https://blueprints.launchpad.net/quantum/+spec/quantum-service-framework)
was landed, as well as support for [highly-available RabbitMQ
queues](https://blueprints.launchpad.net/quantum/+spec/high-available-quantum-queues-in-rabbitmq).
Feature parity gap with nova-network was reduced by the introduction of
a [Security Groups
API](https://blueprints.launchpad.net/quantum/+spec/quantum-security-groups).

**Horizon** saw a lot of changes under the hood, including [unified
configuration](https://blueprints.launchpad.net/horizon/+spec/unify-config).
It now supports [Nova flavor extra
specs](https://blueprints.launchpad.net/horizon/+spec/flavor-extra-specs).
As a first step towards providing cloud admins with more targeted
information, a [system info
panel](https://blueprints.launchpad.net/horizon/+spec/system-info-panel)
was added. **Oslo** (formerly known as openstack-common) also saw a
number of improvements. The config module (cfg) was [ported to
argparse](https://blueprints.launchpad.net/oslo/+spec/cfg-argparse).
Common [service management
code](https://blueprints.launchpad.net/oslo/+spec/service-infrastructure)
was pushed to the Oslo incubator, as well as a generic [policy
engine](https://blueprints.launchpad.net/oslo/+spec/new-policy-language).

That's only a fraction of what will appear in the final release of
Grizzly, scheduled for April 2013. A lot of work was started in the last
weeks but will only land in the next milestone. To get a glimpse of
what's coming up, you can follow the [Grizzly release status
page](http://wiki.openstack.org/releasestatus/) !

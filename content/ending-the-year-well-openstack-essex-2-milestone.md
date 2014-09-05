Title: Ending the year well: OpenStack Essex-2 milestone
Date: 2011-12-20 17:03
Author: Thierry Carrez
Tags: OpenStack
Slug: ending-the-year-well-openstack-essex-2-milestone

2011 is almost finished, and what a year it has been. We started it with
two core projects and one release behind us. During 2011, we got three
releases out of the door, grew from 60 code contributors to about 200,
added three new core projects, and met for two design summits.

The Essex-2 milestone was released last week. Here is our now-regular
overview of the work that made it to OpenStack core projects since the
previous milestone.

Nova was the busiest project. Apart from my work on a new [secure root
wrapper](https://blueprints.launchpad.net/nova/+spec/nova-rootwrap), we 
added a pair of OpenStack API extensions to support the
[creation of snapshots and backups of
volumes](https://blueprints.launchpad.net/nova/+spec/nova-volume-snapshot-backup-api),
the [metadata
service](https://blueprints.launchpad.net/nova/+spec/separate-nova-metadata)
can now run separately from the API node, network limits can now be set
using a [per-network base and a per-flavor
multiplier](https://blueprints.launchpad.net/nova/+spec/bandwidth-rate-limit-multipliers-and-base-limits),
and a small usability feature lets you retrieve the [last
error](https://blueprints.launchpad.net/nova/+spec/lasterror) that
occurred using nova-manage. But Essex is not about new features, it's
more about consistency and stability. On the consistency front, the [HA
network mode was extended to support
XenServer](https://blueprints.launchpad.net/nova/+spec/xenapi-ha-nova-network),
KVM compute nodes now [report
capabilities](https://blueprints.launchpad.net/nova/+spec/kvm-report-capabilities)
to zones like Xen ones, and the Quantum network manager now [supports
NAT](https://blueprints.launchpad.net/nova/+spec/quantum-nat-parity).
Under the hood, [VM state
transitions](https://blueprints.launchpad.net/nova/+spec/nova-vm-state-management)
have been strengthened, the network data model
[has](https://blueprints.launchpad.net/nova/+spec/compute-network-info)
[been](https://blueprints.launchpad.net/nova/+spec/network-info-model)
overhauled, internal interfaces now support [UUID instance
references](https://blueprints.launchpad.net/nova/+spec/internal-uuids),
and unused callbacks have [been
removed](https://blueprints.launchpad.net/nova/+spec/remove-virt-driver-callbacks)
from the virt driver.

The other projects were all busy starting larger transitions (Keystone's
RBAC, Horizon new user experience, and Glance 2.0 API), leaving less
room for essex-2 features. Glance still saw the addition of  a [custom
directory for data
buffering](https://blueprints.launchpad.net/glance/+spec/custom-disk-buffer).
Keystone introduced [global endpoints
templates](https://blueprints.launchpad.net/keystone/+spec/global-templates)
and [swauth-like ACL
enforcement](https://blueprints.launchpad.net/keystone/+spec/keystone-swift-acls).
Horizon added UI support for [downloading RC
files](https://blueprints.launchpad.net/horizon/+spec/cert-download),
while migrating under the hood from [jquery-ui to
bootstrap](https://blueprints.launchpad.net/horizon/+spec/migrate-to-bootstrap),
and adding a [versioning
scheme](https://blueprints.launchpad.net/horizon/+spec/environment-versioning)
for environment/dependencies.

The next milestone is in a bit more than a month: January 26th, 2012.
Happy new year and holidays to all !

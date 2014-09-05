Title: Coming up in OpenStack Cactus...
Date: 2011-03-16 16:06
Author: Thierry Carrez
Tags: OpenStack
Slug: coming-up-in-openstack-cactus

In a bit more than a week, we will hit
[FeatureFreeze](http://wiki.openstack.org/FeatureFreeze) for OpenStack
"Cactus" cycle, so we start to have a good idea of what new features
will make it. The Cactus cycle focus was on stability, so there are
fewer new features compared to Bexar, but the developers still achieved
a lot in a couple of months...

### Swift (OpenStack object storage)

The Swift team really focused and stability and performance improvements
this cycle. I will just single out ﻿the refactoring of the proxy to
make [backend requests
concurrent](https://blueprints.launchpad.net/swift/+spec/cactus-asynchronous-proxy),
and improvements on [sqlite3
indexing](https://blueprints.launchpad.net/swift/+spec/cactus-improved-sqlite3-indexing)
as good examples of this effort.

### Glance (OpenStack image registry and delivery service)

Bexar saw the first release of Glance, and in Cactus it was vastly
improved to match standards we have for the rest of OpenStack:
[logging](https://blueprints.launchpad.net/glance/+spec/logging),
[configuration](https://blueprints.launchpad.net/glance/+spec/use-config-parser)
and
[options](https://blueprints.launchpad.net/glance/+spec/use-optparse)
parsing, use of
[paste.deploy](https://blueprints.launchpad.net/glance/+spec/paste-deploy)
and [non-static
versioning](https://blueprints.launchpad.net/glance/+spec/non-static-versioning),
database
[migrations](https://blueprints.launchpad.net/glance/+spec/registry-db-migration)...
New features include a [CLI
tool](https://blueprints.launchpad.net/glance/+spec/cli-tool) and a new
method for client to [verify
images](https://blueprints.launchpad.net/glance/+spec/image-checksumming).
Glance developers might also sneak in an [authentication
middleware](https://blueprints.launchpad.net/glance/+spec/middleware-authentication)
and support for [HTTPS
connections](https://blueprints.launchpad.net/glance/+spec/support-ssl)
!

### Nova (OpenStack compute)

A lot of the feature work in Nova for Cactus revolved around the
[OpenStack API
1.1](https://blueprints.launchpad.net/nova/+spec/openstack-api-1-1) and
exposing features through XenServer
([migration](https://blueprints.launchpad.net/nova/+spec/xs-migration),
[resize](https://blueprints.launchpad.net/nova/+spec/xs-resize), [rescue
mode](https://blueprints.launchpad.net/nova/+spec/xs-rescue),
[IPv6](https://blueprints.launchpad.net/nova/+spec/xs-ipv6),
[file](https://blueprints.launchpad.net/nova/+spec/xs-fileinject) and
[network](https://blueprints.launchpad.net/nova/+spec/xs-inject-networking)
injection...). We should also have the long-awaited [live
migration](https://blueprints.launchpad.net/nova/+spec/cactus-migration-live)
feature (for KVM), support for [LXC
containers](https://blueprints.launchpad.net/nova/+spec/bexar-nova-containers),
[VHD
images](https://blueprints.launchpad.net/nova/+spec/unified-images),
[multiple](https://blueprints.launchpad.net/nova/+spec/multi-nic)[NICs](https://blueprints.launchpad.net/nova/+spec/multinic-libvirt),
dynamically-configured [instance
flavors](https://blueprints.launchpad.net/nova/+spec/configure-instance-types-dynamically)
or volume storage on [HP/Lefthand
SANs](https://blueprints.launchpad.net/nova/+spec/support-hp-san).
XenAPI should get support for [Vlan network
manager](https://blueprints.launchpad.net/nova/+spec/xenapi-vlan-network-manager)
and [network
injection](https://blueprints.launchpad.net/nova/+spec/xenapi-basic-network-injection).
We hope support for [VMWare/vSphere
hypervisor](https://blueprints.launchpad.net/nova/+spec/hypervisor-vmware-vsphere-support)
will make it.

The rest of the Nova team concentrated on testing, bugfixing (already
115 bugfixes committed to Cactus !) and producing a coherent release, as
evidenced by the work on adding the missing [Ipv6 support for
FlatManager](https://blueprints.launchpad.net/nova/+spec/cactus-flatmanager-ipv6-support)
network model. I should also mention that the groundwork for
[multi-tenant
accounting](https://blueprints.launchpad.net/nova/+spec/multi-tenant-accounting)
and [multiple clusters in a
region](https://blueprints.launchpad.net/nova/+spec/multi-cluster-in-a-region)
also landed in Cactus.

Over the three projects branches, last month we had *more than 2500
commits* by more than 75 developers. Not too bad for a project less than
one-year-old... We'll see the result of this work on Cactus release day,
scheduled April 14.

Title: Summer of OpenStack: the diablo-3 milestone
Date: 2011-07-29 12:46
Author: Thierry Carrez
Tags: OpenStack
Slug: the-diablo-3-milestone

No rest for the OpenStack developers, today saw the release of the July
development efforts for Nova and Glance: the Diablo-3 milestone.

Glance gained two performance options: API servers can now [cache image
data on the local
filesystem](https://blueprints.launchpad.net/glance/+spec/local-image-cache),
and a [delayed
delete](https://blueprints.launchpad.net/glance/+spec/delayed-delete)
feature allows image deletion to happen asynchronously.

With a bit more than 100 trunk commits over the month, Nova gained
support for [multiple
NICs](https://blueprints.launchpad.net/nova/+spec/nova-multi-nic),
FlatDHCP network mode now support a
[high-availability](https://blueprints.launchpad.net/nova/+spec/ha-flatdhcp)
option (read more about it
[here](http://unchainyourbrain.com/openstack/13-networking-in-nova)),
instances can be
[migrated](https://blueprints.launchpad.net/nova/+spec/instance-migration)
and [system usage
notifications](https://blueprints.launchpad.net/nova/+spec/system-usage-records)
were added to the notification framework. Network code was also
[refactored](https://blueprints.launchpad.net/nova/+spec/network-refactoring)
in order to facilitate integration with the new networking projects, and
countless fixes were made in [OpenStack API 1.1
support](https://blueprints.launchpad.net/nova/+spec/openstack-compute-api-11-finalization).

We have one more milestone left (diablo-4) before the final 2011.3
release... still a lot to do !

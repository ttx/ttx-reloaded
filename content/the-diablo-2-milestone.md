Title: June in OpenStack: the diablo-2 milestone
Date: 2011-07-04 09:43
Author: Thierry Carrez
Tags: OpenStack
Slug: the-diablo-2-milestone

About a month ago I commented on the features delivered in the diablo-1
milestone. Last week we released the diablo-2 milestone for your testing
and feature evaluation pleasure.

Most of the [changes to
Glance](https://launchpad.net/glance/diablo/diablo-2) were made under
the hood. In particular the [new WSGI
code](https://blueprints.launchpad.net/glance/+spec/wsgi-refactoring)
from Nova was ported to Glance, and images collections can now be
[sorted](https://blueprints.launchpad.net/glance/+spec/api-results-ordering)
by a subset of the image model attributes. Most of the groundwork to
support Keystone authentication was done, but that should only be
available in diablo-3 !

Those same initial [Keystone
integration](https://blueprints.launchpad.net/nova/+spec/integrate-nova-authn)
steps were also done for Nova, along with plenty of other features. We
now support [distributed
scheduling](https://blueprints.launchpad.net/nova/+spec/distributed-scheduler)
for complex deployments, together with a new [instance referencing
model](https://blueprints.launchpad.net/nova/+spec/nova-instance-referencing).
Was also added during this timeframe: support for [floating
IPs](https://blueprints.launchpad.net/nova/+spec/openstack-api-floating-ips)
(in OpenStack API), a basic mechanism for [pushing notifications
out](https://blueprints.launchpad.net/nova/+spec/notification-system) to
interested parties, [global firewall
rules](https://blueprints.launchpad.net/nova/+spec/provider-firewall),
and an [instance type extra
specs](https://blueprints.launchpad.net/nova/+spec/schedule-instances-on-heterogeneous-architectures)
table that can be used in a capabilities-aware scheduler. More invisible
to the user, we completed efforts to [standardize error
codes](https://blueprints.launchpad.net/nova/+spec/error-codes) and
refactored the OpenStack API
[serialization](https://blueprints.launchpad.net/nova/+spec/nova-api-serialization)
mechanism.

And there is plenty more coming up in diablo-3... scheduled for release
on July 28th.

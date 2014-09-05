Title: OpenStack Essex-1 milestone
Date: 2011-11-14 14:50
Author: Thierry Carrez
Tags: OpenStack
Slug: openstack-essex-1-milestone

Last week saw the delivery of the first milestone of the Essex
development cycle for Keystone, Glance, Horizon and Nova. This early
milestone collected about two months of post-Diablo work... but it's not
as busy in new features as most would think, since a big part of those
last two months was spent releasing OpenStack 2011.3 and brainstorming
Essex features.

Keystone delivered their first milestone as a core project, with a few
new features like support for [additional
credentials](https://blueprints.launchpad.net/keystone/+spec/support-multiple-credentials),
[service
registration](https://blueprints.launchpad.net/keystone/+spec/keystone-service-registration)
and using [certificate-based SSL client authentication to authenticate
services](https://blueprints.launchpad.net/keystone/+spec/2-way-ssl). It
should be easier to upgrade from now on, with support for [database
migrations](https://blueprints.launchpad.net/keystone/+spec/database-migrations).

Glance developers were busy preparing significant changes that will land
in the next milestone. Several bugfixes and a few features made it to
essex-1 though, including the long-awaited [SSL client
connections](https://blueprints.launchpad.net/glance/+spec/support-ssl).
It also moved to [UUID image
identifiers](https://blueprints.launchpad.net/glance/+spec/uuid-image-identifiers).

The Nova essex-1 effort was mostly spent on bugfixing, with [129 bugs
fixed](https://launchpad.net/nova/+milestone/essex-1). New features
include a new [XenAPI SM volume
driver](https://blueprints.launchpad.net/nova/+spec/xenapi-sm-support),
[DHCP support in the Quantum network
manager](https://blueprints.launchpad.net/nova/+spec/quantum-dhcp-parity),
and optional [deferred deletion of
instances](https://blueprints.launchpad.net/nova/+spec/deferred-delete-instance).
Under the hood, the [volume
code](https://blueprints.launchpad.net/nova/+spec/volume-cleanup) was
significantly cleaned up and [XML
templates](https://blueprints.launchpad.net/nova/+spec/xml-templates)
were added to simplify serialization in extensions.

Essex-1 was also the first official OpenStack milestone for Horizon,
also known as the Dashboard. New features include a [instance
details](https://blueprints.launchpad.net/horizon/+spec/instance-detail)
page, support for [managing Nova
volumes](https://blueprints.launchpad.net/horizon/+spec/volumes-interface)
and a new [extensible modular
architecture](https://blueprints.launchpad.net/horizon/+spec/extensible-architecture).
The rest of the effort was spent on catching up with the best of core
projects in
[internationalization](https://blueprints.launchpad.net/horizon/+spec/update-localization),
[developer](https://blueprints.launchpad.net/horizon/+spec/sphinx-docs)
[documentation](https://blueprints.launchpad.net/horizon/+spec/horizon-doc-site),
and QA ([frontend
testing](https://blueprints.launchpad.net/horizon/+spec/frontend-testing)
and [JS unit
tests](https://blueprints.launchpad.net/horizon/+spec/javascript-unit-tests)).

Now, keep your seatbelt fastened, as we are one month away from essex-2,
where lots of new development work is expected to land !

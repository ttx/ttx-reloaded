Title: Features are in: the diablo-4 milestone
Date: 2011-08-31 12:53
Author: Thierry Carrez
Tags: OpenStack
Slug: the-diablo-4-milestone

August was very busy for OpenStack Nova and Glance developers, and the
culmination of those efforts is the delivery of the final feature
milestone of the Diablo development cycle: diablo-4.

Glance [gained](https://launchpad.net/glance/+milestone/diablo-4) final
[integration with the Keystone common authentication
system](https://blueprints.launchpad.net/glance/+spec/authentication),
support for [sharing images between groups of
tenants](https://blueprints.launchpad.net/glance/+spec/shared-images), a
new [notification
system](https://blueprints.launchpad.net/glance/+spec/glance-notifications)
and [i18n](https://blueprints.launchpad.net/glance/+spec/i18n).
[Twelve](https://launchpad.net/nova/+milestone/diablo-4) feature
blueprints were completed in Nova, including final [Keystone
integration](https://blueprints.launchpad.net/nova/+spec/finalize-nova-auth),
the long-awaited capacity to [boot from
volumes](https://blueprints.launchpad.net/nova/+spec/boot-from-volume),
a [configuration
drive](https://blueprints.launchpad.net/nova/+spec/configuration-drive)
to pass information to instances,
[integration](https://blueprints.launchpad.net/nova/+spec/linuxnet-vif-plugging)
[points](https://blueprints.launchpad.net/nova/+spec/nova-quantum-vifid)
for Quantum, KVM [block migration
support](https://blueprints.launchpad.net/nova/+spec/kvm-block-migration),
as well as
[several](https://blueprints.launchpad.net/nova/+spec/os-security-groups)
[improvements](https://blueprints.launchpad.net/nova/+spec/add-remove-securitygroup-instance)
[to](https://blueprints.launchpad.net/nova/+spec/add-options-network-create-os-apis)
the OpenStack API.

Diablo-4 is mostly feature-complete: a few blueprints for standalone
features were granted an exception and will land post-diablo-4, like
volume types or virtual storage arrays [in
Nova](https://launchpad.net/nova/+milestone/diablo-rbp), or like SSL
support [in Glance](https://launchpad.net/glance/+milestone/diablo-rbp).

Now we race towards the release branch point (September 8th) which is
when the Diablo release branch will start to diverge from a newly-open
Essex development branch. The focus is on testing, bug fixing and
consistency... up until September 22, the Diablo release day.

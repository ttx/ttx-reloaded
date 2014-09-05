Title: What will be in OpenStack Bexar release
Date: 2010-12-22 08:45
Author: Thierry Carrez
Tags: OpenStack
Slug: what-will-be-in-openstack-bexar-release

OpenStack is busy with so much development activity it's hard to keep
up.  [42 (!) specs](http://wiki.openstack.org/releasestatus/) were
targeted for the 3-month long [Bexar development
cycle](http://wiki.openstack.org/BexarReleaseSchedule)... and there are
more than 150 active branches. Over the last month alone, we saw 750
commits by 50 different people. Taking a step back, what new features
should you expect to land on February 3rd, in the Bexar release ?

### Swift (OpenStack object storage)

The big news in Swift is support for unlimited object size, through the
implementation of [client-side
chunking](https://blueprints.launchpad.net/swift/+spec/bexar-client-side-chunking).
The only size limit for your objects is now the available size in your
Swift cluster ! You can read more about that exciting feature in [John
Dickinson's blog
post](http://programmerthoughts.com/programming/the-story-of-an-openstack-feature/).
We also hope to ship
[Swauth](https://blueprints.launchpad.net/swift/+spec/bexar-swauth),
DevAuth highly scalable replacement, directly into Swift codebase.
Exposure of most of the [S3 API in
Swift](https://blueprints.launchpad.net/swift/+spec/bexar-s3api) may or
may not make it.

### Glance (OpenStack image registry and delivery service)

The Glance image service will expose a [unified REST
API](https://blueprints.launchpad.net/glance/+spec/unified-api) (no more
distinction between the image registry and the image delivery services).
We will also have the possibility to upload image data and metadata over
[one single
call](https://blueprints.launchpad.net/glance/+spec/api-add-image).
Unified [client
classes](https://blueprints.launchpad.net/glance/+spec/clients) will be
shipped directly in Glance. We also hope to have a [S3
backend](https://blueprints.launchpad.net/glance/+spec/teller-s3-backend)...

### Nova (OpenStack compute)

There is so much coming up in Nova it's hard to summarize. Nova will
[make use of those new Glance client
classes](https://blueprints.launchpad.net/nova/+spec/image-service-use-glance-clients),
obviously. We will support booting VMs from [raw disk
images](https://blueprints.launchpad.net/nova/+spec/raw-disk-images)
(rather than a kernel/ramdisk/image combination) and have a [rescue
mode](https://blueprints.launchpad.net/nova/+spec/rescue-mode) to mount
your faulty disks under a sane environment. We plan to have
[instance](https://blueprints.launchpad.net/nova/+spec/xs-snapshots)
[snapshots](https://blueprints.launchpad.net/nova/+spec/snapshot-instance)
ready. API servers can now
[expose](https://blueprints.launchpad.net/nova/+spec/admin-only-api)
optional admin features (through the --allow\_admin\_api flag), like a
specific XenServer instance
[pause](https://blueprints.launchpad.net/nova/+spec/xs-pause) or
[suspend](https://blueprints.launchpad.net/nova/+spec/xs-suspend)
feature.

Lots of improvements might go unnoticed, like the
[internationalization](https://blueprints.launchpad.net/nova/+spec/i18n-support)
of messages, the standardization on services using eventlet, more robust
[logging](https://blueprints.launchpad.net/nova/+spec/audit-logging),
or the move of the IP allocation [down the
stack](https://blueprints.launchpad.net/nova/+spec/move-ip-allocation).
We'll also finalize some incomplete features, like access to your
[project VLAN through a
VPN](https://blueprints.launchpad.net/nova/+spec/project-vpn), [security
groups](https://blueprints.launchpad.net/nova/+spec/bexar-iptables-security-groups)
that work in all network modes, and
[Hyper-V](https://blueprints.launchpad.net/nova/+spec/austin-microsoft-hyper-v-support)
support.

We hope to have much more: a [web-based serial
console](https://blueprints.launchpad.net/nova/+spec/web-based-serial-console)
to access your VMs,
[ipv6](https://blueprints.launchpad.net/nova/+spec/ipv6-support)
support, the possibility to deploy hardware in a [staging
area](https://blueprints.launchpad.net/nova/+spec/hardware-staging) of
your cloud, support for highly available block volumes through
[Sheepdog](https://blueprints.launchpad.net/nova/+spec/sheepdog-support),
instance
[diagnostics](https://blueprints.launchpad.net/nova/+spec/diagnostics-per-instance)
allowing to retrieve a history of actions on instances, the possibility
to do [live
migration](https://blueprints.launchpad.net/nova/+spec/bexar-migration-live)
in nova-manage, [iSCSI
support](https://blueprints.launchpad.net/nova/+spec/bexar-iscsi-support-xenapi)
for XenAPI... But let's be realistic, not everything will land in time.
What doesn't make it will certainly be in the next release, Cactus,
which will be released in April !

Congrats to our awesome development team for making all this possible.
Those last two months have been a very fun ride for me :)

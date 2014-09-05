Title: A month in OpenStack Diablo: the diablo-1 milestone
Date: 2011-06-02 08:02
Author: Thierry Carrez
Tags: OpenStack
Slug: the-diablo-1-milestone

Back at the OpenStack Design Summit in Santa Clara, we decided to switch
from a 3-month cycle to a 6-month coordinated release cycle, with more
frequent milestones delivery in the middle.

Lately we have been busy adapting the release processes to match the
delivery of the first milestones. Swift 1.4.0 was released last Tuesday,
and today sees the release of the diablo-1 milestone for Nova and
Glance.

What should you expect from diablo-1, just 4 weeks after the design
summit ? In this short timeframe lots of features have been worked on,
and the developers managed to land quite a few of them in time for
diablo-1.

Glance's API was improved to support [filtering of /images and
/images/detail
results](https://blueprints.launchpad.net/glance/+spec/api-results-filtering)
and [limiting and paging of
results](https://blueprints.launchpad.net/glance/+spec/api-limited-results).
This made [support of API
versioning](https://blueprints.launchpad.net/glance/+spec/api-versioning)
necessary. It also grew a [new disk
format](https://blueprints.launchpad.net/glance/+spec/iso-boot) ("iso")
that should ultimately allow to boot ISOs directly in Nova.

On Nova's side, the most notable addition is support for
[snapshotting](https://blueprints.launchpad.net/nova/+spec/snapshot-volume)
and [cloning](https://blueprints.launchpad.net/nova/+spec/clone-volume)
volumes with the EC2 API. The XenServer plugin now supports [Open
vSwitch](https://blueprints.launchpad.net/nova/+spec/xs-ovs), and pause
and suspend capabilities have been [added to the KVM
hypervisor](https://blueprints.launchpad.net/nova/+spec/kvm-pause-suspend).

Now keep your seatbelt fastened, because diablo-2 is set to release on
June 30th.

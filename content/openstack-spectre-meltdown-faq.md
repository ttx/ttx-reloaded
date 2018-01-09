Title: OpenStack Spectre/Meltdown FAQ
Date: 2018-01-08 17:03
Author: Thierry Carrez
Tags: OpenStack, Security
Slug: openstack-spectre-meltdown-faq

## What are Meltdown and Spectre ?

Meltdown and Spectre are the brand names of a series of vulnerabilities
discovered by various security researchers around performance optimization
techniques built in modern CPUs. Those optimizations (involving superscalar
capabilities, out-of-order execution, and speculative branch prediction)
fundamentally create a
[side-channel](https://en.wikipedia.org/wiki/Side-channel_attack) that can
be exploited to deduce the content of computer memory that should normally
not be accessible.

## Why is it big news ?

It's big news because rather than affecting a specific operating system,
it affects most modern CPUs, in ways that cannot be completely fixed
(as you can't physically extract the flawed functionality out of your CPUs).
The real solution is in a new generation of CPU optimizations that will
not exhibit the same flaws while reaching the same levels of performance.
This is unlikely to come soon, which means we'll have to deal with workarounds
and mitigation patches for a long time.

## Why is it business as usual ?

As [Bruce Schneier](https://www.schneier.com/essays/archives/1999/11/a_plea_for_simplicit.html)
says, "you can't secure what you don't understand". As we build more complex
systems (in CPUs, in software, in policies), it is more difficult to build
them securely, and they can fail in more subtle ways. There will always be
new vulnerabilities and new classes of attacks found, and the answer is always
the same: designing defense in depth, keeping track of vulnerabilities found,
and swiftly applying patches. This episode might be big news, but the
remediation is still applying well-known techniques and processes.

## Are those 2 or 3 different vulnerabilities ?

It is actually three different exploitation techniques of the same famility
of vulnerabilities, which need to be protected against separately.

- *CVE-2017-5753* (“bounds check bypass”, or variant 1) is one of the two
*Spectre* variants. It affects specific sequences within compiled applications,
which must be addressed on a per-binary basis. Applications that can be made
to execute untrusted code (e.g. operating system kernels or web browsers) will
need updates as more of those exploitable sequences are found.

- *CVE-2017-5715* (“branch target injection”, or variant 2) is the other
*Spectre* variant. It more generally works by poisoning the CPU branch
prediction cache to induce privileged applications to leak small bits of
information. This can be fixed by a CPU microcode update or by applying
advanced software mitigation techniques (like Google's Retpoline) to the
vulnerable binaries.

- *CVE-2017-5754* (“rogue data cache load”, or variant 3) is also called
*Meltdown*. This technique lets any unprivileged process read kernel memory
(and therefore access information and secrets in other processes running
on the same system). It is the easiest to exploit, and requires patching
the operating system to reinforce isolation of memory page tables at the
kernel level.

## What is the impact of those vulnerabilities for OpenStack cloud users ?

Infrastructure as a service harnesses virtualization and containerization
technologies to present a set of physical, bare-metal resources as virtual
computing resources. It heavily relies on the host kernel security features
to properly isolate untrusted workloads, especially the various virtual
machines running on the same physical host. When those fail (like is the
case here), you can have a hypervisor break. An attacker in a hostile VM
running on an unpatched host kernel could use those techniques to access
data in other VMs running on the same host.

Additionally, if the guest operating system of your VMs is not patched
(or you run a vulnerable application) and run untrusted code on that VM
(or in that application), that code could leverage those vulnerabilities
to access information in memory in other processes on the same VM.

## What should I do as an OpenStack cloud provider ?

Cloud providers should apply kernel patches (from their Linux distribution),
hypervisor software updates (from the distribution or their vendor) and CPU
microcode updates (from their hardware vendor) that workaround or mitigate
those vulnerabilities as soon as they are made available, in order to protect
their users.

## What should I do as an OpenStack cloud user ?

Cloud users should watch for and apply operating system patches for their
guest VMs as soon as they are made available. This advice actually applies
to any computer (virtual or physical) you happen to use (including your phone).

## Are patches available already ?

Some patches are out, some are still due. Kernel patches mitigating the
Meltdown attack are available upstream, but they are significant patches
with lots of side-effects, and some OS vendors are still testing them.
The coordinated disclosure process failed to keep the secret up to the
publication date, which explains why some OS vendors or distributions were
not ready when the news dropped.

It is also important to note that this is likely to trigger a long series
of patches, as the workarounds and mitigation patches are refined to reduce
side-effects and new bugs that those complex patches themselves create. The
best recommendation is to keep an eye on your OS vendor patches (and CPU
vendor microcode updates) for the coming months and apply all patches quickly.

## Is there a performance hit in applying those patches ?

The workarounds and mitigation techniques are still being developed, so it
is a little early to say, and it will always depend on the exact workload.
However, since the basic flaw here lies in performance optimization techniques
in CPUs, most workarounds and mitigation patches should add extra checks,
steps and synchronization that will undo some of that performance
optimization, resulting in a performance hit.

## Is there anything that should be patched on the OpenStack side ?

While OpenStack itself is not directly affected, it is likely that some of
the patches that are and will be developed to mitigate those issues will
require optimizations in software code to limit the performance penalty.
Keep an eye on our stable branches and/or your OpenStack vendor patches
to make sure you catch any of those.

Those vulnerabilities also shine some light on the power of side-channel
attacks, which shared systems are traditionally more vulnerable to. Security
research is likely to focus on such class of issues in the near future,
potentially discovering side-channel security attacks in OpenStack that
will need to be fixed.

## Where can I learn more ?

You can find lots of explanations over the Internet. To understand the basic
flaw and the CPU technologies involved, I recommend reading
[Eben Upton's great post](https://www.raspberrypi.org/blog/why-raspberry-pi-isnt-vulnerable-to-spectre-or-meltdown/).
If that's too deep or you need a good analogy to tell your less-technical
friends, I find
[this one by Robert Merkel](https://medium.com/@rgmerk/an-explanation-of-meltdown-and-spectre-for-non-programmers-7e98b0a28da4) not too bad.

For technical details on the vulnerability themselves,
[Jann Horn's post on Google Project Zero blog](https://googleprojectzero.blogspot.fr/2018/01/reading-privileged-memory-with-side.html)
should be first on your list. You can also read the
[Spectre](https://spectreattack.com/spectre.pdf)
and [Meltdown](https://meltdownattack.com/meltdown.pdf) papers.

For more information on the various mitigation techniques, I recommend
starting with
[this article from Google's Security blog](https://security.googleblog.com/2018/01/more-details-about-mitigations-for-cpu_4.html).
For information about Linux kernel patches in particular, I recommend
[Greg Kroah-Hartman's post](http://kroah.com/log/blog/2018/01/06/meltdown-status/).

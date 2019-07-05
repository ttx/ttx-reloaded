Title: Open source in 2019, Part 2/3
Date: 2019-07-08 15:50
Author: Thierry Carrez
Tags: Open source
Slug: open-source-2019-part2

21 years in, the landscape around open source evolved a lot. In
[part 1](https://ttx.re/open-source-2019-part1.html) of this 3-part series,
I explained all of open source benefits and why I think open source is
necessary today. In this part, I'll argue that **open source is not enough**.

## The relative victory of open source

All the benefits detailed in
[part 1](https://ttx.re/open-source-2019-part1.html) really explain why open
source became so popular in the last 15 years. Open source is everywhere today.
It has become the default way to build and publish software. You can find open
source on every server, you can find open source on every phone... Even
Microsoft, the company which basically invented proprietary software, is
heavily adopting open source today, with great success. By all accounts,
open source won.

But... has it, really ?

The server, and by extension the computing, networking, and storage
infrastructure, are unquestionably dominated by open source. But the
growing share of code running operations for this infrastructure software
is almost always kept private. The glue code used to provide users access
to this infrastructure (what is commonly described as "cloud computing")
is more often than not a trade secret. And if you look to the other side,
the desktop (or the user-side applications in general) are still
overwhelmingly driven by proprietary software.

Even contemplating what are generally considered open source success
stories, winning can leave a bitter taste in the mouth. For example, looking
at two key tech successes of the last 10 years, Amazon Web Services and
Android, they both are heavily relying on open source software. They
are arguably a part of this *success of open source* picture I just
painted. But if you go back to
[part 1](https://ttx.re/open-source-2019-part1.html) and look at all
the user benefits I listed, the users of AWS and Android don’t really
enjoy them all. As an AWS user, you don't have *transparency*: you can’t
really look under the hood and understand how AWS runs things, or why the
service behaves the way it does. As an Android user, you can’t really
engage with Android upstream, contribute to the creation of the software
and make sure it serves your needs better tomorrow.

So open source won and is ubiquitous... however in most cases, users are
denied some of the key benefits of open source. And looking at what is
called "open source" today, one can find lots of twisted production models.
By "twisted", I mean models where some open source benefits go missing,
like the ability to efficiently engage in the community.

For example, you find *single-vendor* open source, where the
software is controlled by a single company doing development behind
closed doors. You find *open-core* open source, where advanced features
are reserved for a proprietary version and the open source software is
used as a trial edition. You find open source *code drops*, where an
organization just periodically dumps their code to open-wash it with
an open source label. You find *fire and forget* open source, where people
just publish once on GitHub with no intention of ever maintaining the code.
How did we get here?

## Control or community

What made open source so attractive to the software industry was the
promise of the community. An engaged community that would help them write
the software, build a more direct relationship that would transcend classic
vendor links, and help you promote the software. The issue was, those
companies still very much wanted to keep control: of the software, of the
design, of the product roadmap, and of the revenue. And so, in reaction to
the success of open source, the software industry evolved a way to produce
open source software that would allow them to retain control.

But the fact is... you can’t really have control **and** community. The
exclusive control by a specific party over the code is discouraging other
contributors from participating. The external community is considered as
free labor, and is not on a level playing field compared to contributors
on the inside, who really decide the direction of the software. This is
bound to create frustration. This does not make a sustainable community,
and ultimately does not result in sustainable software.

The *open-core* model followed by some of those companies creates an
additional layer of community tension. At first glance, keeping a set
of advanced features for a proprietary edition of the software sounds
like a smart business model. But what happens when a contributor proposes
code that would make the "community edition" better ? Or when someone starts
to question why a single party is capitalizing on the work of "the community"?
In the best case, this leads to the death of the community, and in the worst
case this leads to a fork... which makes this model particularly brittle.

By 2019, I think it became clearer to everyone that they have to choose
between keeping control and growing a healthy community. However most
companies chose to retain control, and abandon the idea of true community
contribution. Their goal is to keep reaping the marketing gains of calling
their software open source, of pretending to have all the benefits associated
with the open source label, while applying a control recipe that is much
closer to proprietary software than to the original freedoms and rights
associated with free software and open source.

## How open source is built impacts the benefits users get

So the issue with twisted production models like single-vendor or open-core is
that you are missing some benefits, like *availability*, or *sustainability*,
or *self-service*, or the ability to engage and influence the direction of
the software. The software industry adapted to the success of open source:
it adopted open source licenses but little else, stripping users of the
benefits associated with open source while following the letter of the
open source law.

How is that possible?

The issue is that free software and open source both addressed solely the
angle of freedom and rights that users get with the end product, as conveyed
through software licenses. They did not mandate **how** the software was to
be built. They said nothing about **who** really controls the creation of
the software. And how open source is built actually has a major impact on
the benefits users get out of the software.

The sad reality is, in this century, most open source projects are actually
closed one way or the other: their core development may be done behind
closed doors, or their governance may be locked down to ensure permanent
control by the main sponsor. Everyone produces open source software, but
projects developed by a truly open community have become rare.

And yet, with truly open communities, we have an open source production
model that guarantees all the benefits of free and open source software.
It has a number of different names. I call it **open collaboration**:
the model where a community of equals contributes to a commons on a level
playing field, generally under an open governance and sometimes the asset
lock of a neutral non-profit organization. No reserved seats, no elite
group of developers doing design behind closed doors. Contribution is the
only valid currency.

Open collaboration used to be the norm for free and open source software
production. While it is more rare today, the success of recent open
infrastructure communities like [OpenStack](https://www.openstack.org) or
[Kubernetes](https://kubernetes.io) proves that this model is still viable
today at very large scale, and can be business-friendly. This model
guarantees all the open source benefits I listed in
[part 1](https://ttx.re/open-source-2019-part1.html), especially
sustainability (not relying on a single vendor), and the ability
for anyone to engage, influence the direction of the software, and
make sure it addresses their future needs.

## Open source is not enough

As much as I may regret it, the software industry is free to release their
closely-developed software under an open source license. They have every
right to call their software "open source", as long as they comply with
the terms of an [OSI-approved license](https://opensource.org/licenses).
So if we want to promote good all-benefits-included open source against
twisted some-benefits-withheld open source, F/OSS advocates will need
to regroup, work together, reaffirm the open source definition and
build additional standards on top of it, beyond "open source".

This will be the theme of the last part in this series, to be published
next week. Thank you for reading so far!

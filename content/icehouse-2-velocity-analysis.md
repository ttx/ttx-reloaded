Title: Icehouse-2 velocity analysis
Date: 2014-02-03 16:08
Author: Thierry Carrez
Tags: OpenStack
Slug: icehouse-2-velocity-analysis

Looking at our recently-concluded *icehouse-2* development timeframe, we
landed far less features and bugfixes than we wanted and expected. That
created concerns about us losing our velocity, so I run a little
analysis to confirm or deny that feeling.

### Velocity loss ?

If we compare *icehouse* to the *havana* cycle and focus on implemented
blueprints (not the best metric), it is pretty obvious that *icehouse-2*
was disappointing:

> havana-1: 63  
>  havana-2: 100  
>  icehouse-1: 69  
>  icehouse-2: 50

Using the first milestone as a baseline (growth of 10% expected), we
should have been at 110 blueprints, so we are at 45% of the expected
results. That said, looking at bugs gives a slightly different picture:

> havana-1: 671  
>  havana-2: 650  
>  icehouse-1: 738  
>  icehouse-2: 650

The first milestone baseline again gives a 10% expected growth, which
means the target was 715 bugs... but we "only" fixed 650 bugs (like in
*havana-2*). So on the bugfixes front, we are at 91% of the expected
result.

### Comparing with grizzly

But *havana* is not really the cycle we should compare *icehouse* with.
We should compare with another cycle where the end-of-year holidays hit
during the -2 milestone development... so ***grizzly***. Let's look at
the number of commits (ignoring merges), for a number of projects that
have been around since then. Here are the results for nova:

> nova grizzly-1: 549 commits  
>  nova grizzly-2: 465 commits  
>  nova icehouse-1: 548 commits  
>  nova icehouse-2: 282 commits

Again using the -1 milestone as a baseline for expected growth (here
+0%), nova in *icehouse-2* ended up at 61% of the expected number of
commits. The results are similar for neutron:

> neutron grizzly-1: 155 commits  
>  neutron grizzly-2: 128 commits  
>  neutron icehouse-1: 203 commits  
>  neutron icehouse-2: 110 commits

Considering the -1 milestones gives an expected growth in commits
between *grizzly* and *icehouse* of +31%. *Icehouse-2* is at 66% of
expected result. So not good but not catastrophic either. What about
cinder ?

> cinder grizzly-1: 86 commits  
>  cinder grizzly-2: 54 commits  
>  cinder icehouse-1: 175 commits  
>  cinder icehouse-2: 119 commits

Now that's interesting... Expected cinder growth between *grizzly* and
*icehouse* is +103%. *Icehouse-2* scores at 108% of the expected,
*grizzly*-based result.

> keystone grizzly-1: 95 commits  
>  keystone grizzly-2: 42 commits  
>  keystone icehouse-1: 116 commits  
>  keystone icehouse-2: 106 commits

That's even more apparent with keystone, which had a quite disastrous
*grizzly-2*: expected growth is +22%, Icehouse-2 is at 207% of the
expected result. Same for Glance:

> glance grizzly-1: 100 commits  
>  glance grizzly-2: 38 commits  
>  glance icehouse-1: 98 commits  
>  glance icehouse-2: 89 commits

Here we expect 2% less commits, so based on *grizzly-2* we should have
had 37 commits... *icehouse-2* here is at 240% !

In summary, while it is quite obvious that we delivered far less than we
wanted to, due to the holidays and the recent gate issues, from a
velocity perspective *icehouse-2* is far from being disastrous if you
compare it to the last development cycle where the holidays happened at
the same time in the cycle. Smaller projects in particular have handled
that period significantly better than last year.

We just need to integrate the fact that the October - April cycle
includes a holiday period that will reduce our velocity... and lower our
expectations as a result.

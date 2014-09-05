Title: Improving Nova privilege escalation model, part 2
Date: 2011-11-25 11:00
Author: Thierry Carrez
Tags: OpenStack
Slug: improving-nova-privilege-escalation-model-part-2

In the [previous post in this
series]({filename}/improving-nova-privilege-escalation-model-part-1.md)
we explored the current privilege escalation model used in OpenStack
Compute (Nova), and discussed its limitations. Now that we are able to
plug an alternative model (thanks to the *root\_helper* option), we'll
discuss in this post what features this one should have. If you think we
need more, please comment !

#### Command filters

The most significant issue with the current model is that *sudoers*
filters the executable used, but not the arguments. To fix that, our
alternative model should allow precise argument filtering so that only
very specific commands are allowed. It should use lists of filters: if
one matches, the command is executed.

The basic *CommandFilter* would just check that the executable name
matches (which is what sudoers does). A more advanced *RegexpFilter*
would check that the number of arguments is right and that they all
match provided regular expressions.

Taking that concept a step further, you should be able to plug any type
of advanced filter. You may want to check that the argument to the
command is an existing directory. Or one that is owned by a specific
user. The framework should allow developers to define their own
*CommandFilter* subclasses, to be as precise as they want when filtering
the most destructive commands.

#### Running as

In some cases, Nova runs, as *root*, commands that it should just run as
a different user. For example, it runs *kill* with *root* rights to
interact with *dnsmasq* processes (owned by the *nobody* user). It
doesn't really need to run *kill* with *root* rights at all. Filters
should therefore also allow to specify a lower-privileged user a
specific matching command should run under.

#### Shipping filters in Nova code

Filter lists should live within Nova code and be deployed by packaging,
rather than live in packaging. That allows people adding a new escalated
command to add the corresponding filter in the same commit.

#### Limiting commands based on deployed nodes

As mentioned in the [previous
post]({filename}/improving-nova-privilege-escalation-model-part-1.md),
*nova-api* nodes don't actually need to run any command as *root*, but
in the current model their *nova* user is still allowed to run plenty of
them. The solution for that is to separate the command filters based on
the type of node that is allowed to run them, in different files. Then
deploy the *nova-compute* filters file only on *nova-compute* nodes, the
*nova-volume* filters file only on *nova-volume* nodes... A pure
*nova-api* node will end up with no filters being deployed at all,
effectively not being allowed any command as root. So this can be solved
by smart packaging of filter files.

#### Missing features ?

Those are the features that I found useful for our alternative privilege
escalation model. If you see others, please comment here ! I'd like to
make sure all the useful features are included. In the next post, we'll
discuss a proposed Python implementation of this framework, and the
challenges around securing it.

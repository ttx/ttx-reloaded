Title: Improving Nova privilege escalation model, part 3
Date: 2011-11-30 14:29
Author: Thierry Carrez
Tags: OpenStack
Slug: improving-nova-privilege-escalation-model-part-3

In the previous two posts of this series, we explored the [deficiencies
of the current
model]({filename}/improving-nova-privilege-escalation-model-part-1.md)
and the [features of an alternative
implementation]({filename}/improving-nova-privilege-escalation-model-part-2.md).
In this last post, we'll discuss the advantages of a Python
implementation and open discussion on how to secure it properly.

#### Python implementation

It's quite easy to implement the features that were mentioned in the
previous post in Python. The main advantage of doing so is that the code
can happily live inside Nova code, in particular the filters definition
files can be implemented as Python modules that are loaded if present.
That solves the issue of shipping definitions within Nova and also the
separation of allowed commands based on locally-deployed nodes. The code
is simple and easy to review. The trick is to make sure that no
malicious code can be injected in the elevated rights process. This is
why I'd like to present a model and open it for comments in the
community.

#### Proposed security model

The idea would be to have Nova code optionally use "sudo nova-rootwrap"
instead of "sudo" as the *root\_helper.* A generic *sudoers* file would
allow the *nova* user to run */usr/bin/nova-rootwrap* as *root*, while
stripping environment variables like *PYTHONPATH*. To load its filters
definitions, *nova-rootwrap* would try to import a set of predefined
modules (like *nova.rootwrap.compute*), but if those aren't present, it
should ignore them. Can this model be abused ?

The obvious issue is to make sure *sys.path* (the set of directories
from which Python imports its modules) is secure, so that nobody can
insert their own modules in the process. I've given some thoughts to
various checks, but actually there is no way around trusting the default
*sys.path* you're given when you start *python* as *root* from a cleaned
env. If that's compromised, you're toasted the moment you "import sys"
anyway. So using *sudo* to only allow */usr/bin/nova-rootwrap* and
cleaning the environment should be enough. Or am I missing something ?

#### Insecure mode ?

One thing we could do is check that *sys.path* all belongs to *root* and
refuse to run in the case it's not. That would tell the user that his
setup is insecure (potentially allowing him to bypass that by running
"sudo nova-rootwrap --insecure" as the *root\_helper*). But that's a
convenience to detect insecure setups, not a security addition (the fact
that it doesn't complain doesn't mean you're safe, it could mean you're
already compromised).

#### Test mode ?

For tests, it's convenient to allow to run code from branches. To allow
this (unsafe) mode, you would tweak *sudoers* to allow it to run
*\$BRANCH/bin/nova-rootwrap* as *root*, and prepend ".." to *sys.path*
in order to allow modules to be loaded from *\$BRANCH* (maybe requiring
*--insecure* mode for good measure). It sounds harmless, since if you
run from */usr/bin/nova-rootwrap* you can assume that */usr* is safe...
Or should that idea be abandoned altogether ?

#### Audit

Nothing beats peer review when it comes to secure design. I call all
Python module-loading experts and security white-hats out there: would
this work ? Are those safe assumptions ? How much do you like *insecure*
and *test* modes ? Would you suggest something else ? If you're one of
those that can't think in words but require code, you can get a glimpse
of work in progress
[here](https://github.com/ttx/nova/compare/master...root-wrapper). It
will all be optional (and not used by default), so it can be added to
Nova without much damage, but I'd rather do it right from the beginning
:) Please comment !
